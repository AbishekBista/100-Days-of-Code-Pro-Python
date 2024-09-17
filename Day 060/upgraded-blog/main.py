from flask import Flask, render_template, request
import smtplib
import requests
from secret import my_email, password

all_posts = requests.get("https://api.npoint.io/3696de97e7d5362e27fd").json()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', all_posts=all_posts)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['POST', 'GET'])
def contact():
    if request.method == 'GET':
        return render_template('contact.html', heading_text="Contact Me")
    elif request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        tel = request.form['tel']
        message = request.form['message']
        with smtplib.SMTP(host='smtp.gmail.com', port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=my_email, msg=f'Subject:New message\n\nName: {name}\nEmail: {email}\nPhone No.: {tel}\nMessage: {message}')
        return render_template('contact.html', heading_text="Successfully sent your message")

@app.route('/post/<int:id>')
def post(id):
    post = all_posts[id - 1]
    return render_template('post.html', post=post)

if __name__ == "__main__":
    app.run(debug=True)