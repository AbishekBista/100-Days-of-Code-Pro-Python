from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)

@app.route('/')
def home_page():
    year = datetime.datetime.today().year
    print(year)
    random_number = random.randint(0, 10)
    return render_template('index.html', num=random_number, year=year)

@app.route('/guess/<name>')
def guess_page(name):

    response = requests.get(f"https://api.agify.io/?name={name}")
    response.raise_for_status()
    data = response.json()
    age = data['age']

    response = requests.get(f"https://api.genderize.io?name={name}")
    response.raise_for_status()
    data = response.json()
    gender = data['gender']

    return render_template('guess.html', name=name.title(), gender=gender, age=age)

@app.route('/football/<num>')
def football_page(num):
    print(num)
    response = requests.get("https://api.npoint.io/3696de97e7d5362e27fd")
    response.raise_for_status()
    all_facts = response.json()
    return render_template('football.html', all_facts=all_facts)

if __name__ == "__main__":
    app.run(debug=True)