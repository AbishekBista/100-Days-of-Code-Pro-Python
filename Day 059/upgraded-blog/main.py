from flask import Flask, render_template
import requests

all_posts = requests.get("https://api.npoint.io/3696de97e7d5362e27fd").json()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', all_posts=all_posts)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/post/<int:id>')
def post(id):
    post = all_posts[id - 1]
    return render_template('post.html', post=post)

if __name__ == "__main__":
    app.run(debug=True)