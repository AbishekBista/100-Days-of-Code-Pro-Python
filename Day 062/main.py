from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.fields.html5 import URLField
from wtforms.validators import DataRequired
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe = StringField(label='Cafe name', validators=[DataRequired()])
    location_url = URLField(label='URL', validators=[DataRequired()])
    opening_time = StringField(label='Opening Time eg. 8 AM', validators=[DataRequired()])
    closing_time = StringField(label='Closing Time eg. 5:30 PM', validators=[DataRequired()])
    coffee_rating = SelectField(label='Coffee Rating', choices=['☕', '☕☕', '☕☕☕', '☕☕☕☕', '☕☕☕☕☕'], default='☕', validators=[DataRequired()])
    wifi_rating = SelectField(label='WiFi Strength Rating', choices=['💪', '💪💪', '💪💪💪', '💪💪💪💪', '💪💪💪💪💪'], default='💪', validators=[DataRequired()])
    power_outlet_rating = SelectField(label='Power Outlet Rating', choices=['🔌', '🔌🔌', '🔌🔌🔌', '🔌🔌🔌🔌', '🔌🔌🔌🔌🔌'], default='🔌', validators=[DataRequired()])
    submit = SubmitField('Submit')


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        cafe = request.form['cafe']
        location_url = request.form['location_url']
        opening_time = request.form['opening_time']
        closing_time = request.form['closing_time']
        coffee_rating = request.form['coffee_rating']
        wifi_rating = request.form['wifi_rating']
        power_outlet_rating = request.form['power_outlet_rating']

        with open('cafe-data.csv', mode='a', encoding='utf-8') as csv_file:
            csv_file.write(f"\n{cafe},{location_url},{opening_time},{closing_time},{coffee_rating},{wifi_rating},{power_outlet_rating}")

        with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
            csv_data = csv.reader(csv_file, delimiter=',')
            list_of_rows = []
            for row in csv_data:
                list_of_rows.append(row)
        return render_template('cafes.html', cafes=list_of_rows)
   
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
