from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length



app = Flask(__name__)
app.secret_key = "Hello there"


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=["POST", "GET"])
def login():
    class MyForm(FlaskForm):
        email = StringField(label='Email', validators=[DataRequired(), Email()])
        password = PasswordField(label='Password', validators=[DataRequired(), Length(min=8)])
        submit = SubmitField(label="Log In")

    form = MyForm()
    if form.validate_on_submit():
        password="12345678"
        email="admin@email.com"

        entered_email = form.email.data
        entered_password = form.password.data

        if password == entered_password and email == entered_email:
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)