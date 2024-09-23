from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from sqlalchemy.orm import DeclarativeBase
from datetime import datetime

class Base(DeclarativeBase):
    pass

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap(app)

##CONNECT TO DB
db = SQLAlchemy(model_class=Base)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()


##CONFIGURE TABLE
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)


##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    author = StringField("Your Name", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


@app.route('/')
def get_all_posts():
    with app.app_context():
        posts = BlogPost.query.all()
        print(posts)
        return render_template("index.html", all_posts=posts)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    with app.app_context():
        posts = BlogPost.query.all()
    print(f'we are here {posts}')
    for blog_post in posts:
        if blog_post.id == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route('/new-post', methods=['GET', 'POST'])
def new_post():
    form=CreatePostForm()
    heading = 'Create a New Post'
    if form.validate_on_submit():
        date = datetime.now().strftime('%B %d, %Y')
        title = request.form['title']
        subtitle = request.form['subtitle']
        author = request.form['author']
        img_url = request.form['img_url']
        body = request.form['body']

        new_blog = BlogPost(
            title=title,
            subtitle=subtitle,
            author=author,
            date=date,
            img_url=img_url,
            body=body
        )

        with app.app_context():
            db.session.add(new_blog)
            db.session.commit()
            return redirect('/')

    
    return render_template('make-post.html', form=form, heading=heading, url=url_for('new_post'))

@app.route('/edit_post/<int:post_id>', methods=['GET', 'POST'])
def edit_post(post_id):
    heading = 'Edit Post' 
    with app.app_context():
        post = BlogPost.query.filter_by(id=post_id).first()
        form = CreatePostForm(
            title=post.title,
            subtitle=post.subtitle,
            img_url=post.img_url,
            author=post.author,
            body=post.body
        )
        if form.validate_on_submit():
            post.title = form.title.data
            post.subtitle = form.subtitle.data
            post.img_url = form.img_url.data
            post.author = form.author.data
            post.body = form.body.data
            db.session.commit()
            print(post.title)
            return redirect(f"/post/{post_id}")
    return render_template('make-post.html', heading=heading, form=form, url=url_for('edit_post', post_id=post_id))


@app.route('/delete/<int:id>')
def delete(id):
    with app.app_context():
        post_to_delete = BlogPost.query.get(id)
        db.session.delete(post_to_delete)
        db.session.commit()
        return redirect("/")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)