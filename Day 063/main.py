from flask import Flask, render_template, request, redirect, url_for

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-book-collection.db'
db.init_app(app)

class Book(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(unique=True, nullable=False)
    author: Mapped[str] = mapped_column(nullable = False)
    rating: Mapped[float] = mapped_column(nullable = False)

@app.route('/',)
def home():
        with app.app_context():
            #db.create_all()
            all_books = db.session.query(Book).all()
        return render_template('index.html', all_books=all_books)



@app.route("/add", methods=['POST', 'GET'])
def add():
    if request.method == "POST":
        name = request.form['name']
        author = request.form['author']
        rating = request.form['rating']
        new_book =  Book(title=name, author=author, rating=rating)
        with app.app_context():
            db.session.add(new_book)
            db.session.commit()
        return redirect("/")
    
    return render_template('add.html')

@app.route("/edit", methods=['POST', 'GET'])
def edit():
    id = request.args.get('id')
    if request.method == "POST":    
        with app.app_context():
            print("I'm inside post method")
            book_to_update = Book.query.filter_by(id=id).first()
            print(book_to_update.title)
            book_to_update.rating = float(request.form['rating'])
          
            db.session.commit()
            return redirect("/")

    if request.method == "GET":
        with app.app_context():
            book_to_update = Book.query.filter_by(id=id).first()
            print(book_to_update.title)   
        return render_template('edit.html', book=book_to_update)

@app.route("/delete")
def delete():
    id = request.args.get('id')
    with app.app_context():
        book_to_delete = Book.query.get(id)
        db.session.delete(book_to_delete)
        db.session.commit()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)

