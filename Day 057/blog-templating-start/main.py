from flask import Flask, render_template
import requests
from post import Post


app = Flask(__name__)

response = requests.get("https://api.npoint.io/3696de97e7d5362e27fd").json()
all_facts = []

for fact in response:
    fact_object = Post(fact['id'], fact['title'], fact['subtitle'], fact['body'])
    all_facts.append(fact_object)

@app.route('/')
def home():
    print(all_facts)
    return render_template("index.html", all_facts=all_facts)

@app.route('/post/<int:id>')
def post(id):
    post = all_facts[id - 1]
    return render_template("post.html", post=post)

if __name__ == "__main__":
    app.run(debug=True)
