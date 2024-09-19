from flask import Flask
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

with app.app_context():
    # db.create_all()
    new_book = Book(id=1, title='Great Man', author='Abishek Bista', rating=10.0)
    book = db.session.get(Book, ident=1)
    print(book.title)


