from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
from secret import API_KEY


class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///films-collection.db'
Bootstrap(app)
db.init_app(app)

class EditForm(FlaskForm):
    rating = StringField(label='Rating', validators=[DataRequired()])
    review = StringField(label='Review', validators=[DataRequired()])
    submit = SubmitField(label='Done')

class AddForm(FlaskForm):
    title = StringField(label='Movie Title', validators=[DataRequired()])
    add_movie = SubmitField(label='Add movie')


class Movie(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(unique=True, nullable=False)
    year: Mapped[int] = mapped_column(nullable = False)
    description: Mapped[str] = mapped_column(nullable = False)
    rating: Mapped[float] = mapped_column(nullable = True)
    ranking: Mapped[int] = mapped_column(nullable = True)
    review: Mapped[str] = mapped_column(nullable = True)
    img_url: Mapped[str] = mapped_column(nullable = False)


@app.route("/")
def home():
    with app.app_context():
        # db.create_all()
        # new_movie = Movie(
        #     title="Phone Booth",
        #     year=2002,
        #     description="Publicist Stuart Shepherd finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help. Stuart's negotiation with the caller leads to a jaw-dropping climax",
        #     rating=7.3,
        #     ranking=10,
        #     review="My favorite character was the caller.",
        #     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
        # )
        # db.session.add(new_movie)
        # db.session.commit()
        all_movies = db.session.query(Movie).order_by(Movie.rating)
        movie_count = db.session.query(Movie).count()
        for index, movie in enumerate(all_movies):
            movie.ranking = movie_count - index
        return render_template('index.html', all_movies=all_movies)

@app.route('/edit', methods=['POST', 'GET'])
def edit():
    id = request.args.get('id')
    if request.method == "POST":    
        with app.app_context():
            print("I'm inside post method")
            movie_to_update = Movie.query.filter_by(id=id).first()
            print(movie_to_update.title)
            movie_to_update.rating = float(request.form['rating'])
            movie_to_update.review = request.form['review']
          
            db.session.commit()
            return redirect("/")

    if request.method == "GET":
        form=EditForm()
        with app.app_context():
            movie_to_update = Movie.query.filter_by(id=id).first()
            print(movie_to_update.title)   
        return render_template('edit.html',form=form, movie=movie_to_update)

@app.route('/delete')
def delete():
    id = request.args.get('id')
    with app.app_context():
        movie_to_delete = Movie.query.get(id)
        db.session.delete(movie_to_delete)
        db.session.commit()
    return redirect("/")

@app.route('/add', methods=['POST', 'GET'])
def add():
    form = AddForm()
    if form.validate_on_submit():
        movie_title = request.form['title']
        url = f"https://api.themoviedb.org/3/search/movie?query={movie_title}"
        headers = {
            'accept': 'application/json',
            'Authorization': API_KEY
        }

        response = requests.get(url, headers=headers)
        data = response.json()
        return render_template("select.html", all_movie=data['results'])
    
    id = request.args.get('id')
    if id != None:
        url = f"https://api.themoviedb.org/3/movie/{id}"
        headers = {
            'accept': 'application/json',
            'Authorization': API_KEY
        }

        response = requests.get(url, headers=headers)
        data = response.json()

        title = data['original_title']
        img_url= data['backdrop_path']
        year = int(data['release_date'].split("-")[0])
        description = data['overview']

        print(title, img_url, year, description)

        with app.app_context():
            new_movie = Movie(
                title=title,
                year=year,
                description=description,
                img_url=f"https://image.tmdb.org/t/p/w500{img_url}"
            )
            db.session.add(new_movie)
            db.session.commit()
            movie_to_update = Movie.query.filter_by(title=title).first()
            form = EditForm()
            return render_template('edit.html', form=form, movie=movie_to_update)
        
    return render_template('add.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
