from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from random import randint
from secret import API_KEY

class Base(DeclarativeBase):
    pass

app = Flask(__name__)
db = SQLAlchemy(model_class=Base)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    db.create_all()

##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/random")
def random():
    with app.app_context():
        cafeRecord = Cafe.query.count()
        random_number = randint(0, cafeRecord - 1)
        print(f' I am here {random_number}')
        cafe_record = Cafe.query.get(random_number)
        return jsonify(cafe = cafe_record.to_dict())

@app.route('/all')
def all():
    with app.app_context():
        cafe_records = Cafe.query.all()
        return jsonify(cafes = [record.to_dict() for record in cafe_records])
    
@app.route('/search')
def search():
    loc = request.args.get('loc')
    with app.app_context():
        record = Cafe.query.filter_by(location=loc).first()
        if record == None:
            return jsonify(error = {
                "Not Found": "Sorry, we don't have a cafe at that location."
            }), 404
        return jsonify(cafe = record.to_dict())

@app.route('/add', methods=['POST'])
def add():
    api_key = request.args.get('api-key')
    new_cafe = Cafe(
        name = request.form['name'],
        map_url = request.form['map_url'],
        img_url = request.form['img_url'],
        location = request.form['location'],
        seats = request.form['seats'],
        has_toilet = bool(request.form['has_toilet']),
        has_wifi = bool(request.form['has_wifi']),
        has_sockets = bool(request.form['has_sockets']),
        can_take_calls = bool(request.form['can_take_calls']),
        coffee_price = request.form['coffee_price'],
    )

    if api_key == API_KEY:
        with app.app_context():
            db.session.add(new_cafe)
            db.session.commit()

            return jsonify(response = {
                "success": "Successfully added the new cafe."
            })
    else:
        return jsonify({
            "error": "Sorry, that's not allowed. Make sure you have the correct API key."
        }), 403

@app.route('/update-price/<int:id>', methods=['PATCH'])
def update_price(id):
    new_price = request.args.get('new_price')
    
    cafe_to_update = Cafe.query.filter_by(id=id).first()
    if cafe_to_update == None:
        return jsonify(error = {
            "Not Found": "Sorry, a cafe with that ID was not found in the database."
        }), 404
    
    cafe_to_update.coffee_price = new_price
    db.session.commit()
    return jsonify({
        "success": "Successfully updated the price."
    })

@app.route('/delete/<int:id>', methods=['DELETE'])
def delete(id):
    api_key = request.args.get('api-key')
    if api_key == API_KEY:
        cafe_to_delete = Cafe.query.filter_by(id=id).first()
        if cafe_to_delete:
            db.session.delete(cafe_to_delete)
            db.session.commit()
            return jsonify({
                "success": f"Cafe with ID {id} successfully deleted."
            })
        else:
            return jsonify(error = {
                "Not Found": "Sorry, a cafe with that ID was not found in the database"
            }), 404
    else:
        return jsonify({
            "error": "Sorry, that's not allowed. Make sure you have the correct API key."
        }), 403



if __name__ == '__main__':
    app.run(debug=True)
