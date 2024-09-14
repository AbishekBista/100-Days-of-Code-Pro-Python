from flask import Flask
import random

app = Flask(__name__)

random_number = random.randint(0, 9)

@app.route('/')
def show_home_page():
    return '''
        <h1>Guess a number between 0 and 9</h1>
        <img src="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExdDhwYWQ3NTliOXV3amJkc2ltdndjM2wzMTg2MTFmdnkweWVwbnRhYSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/qnpB8DWzjTE02uxMGz/giphy.gif" width="300" />
            '''

@app.route('/<int:number>')
def guess_number(number):
    if number > random_number:
        return '''
            <h1>Too high</h1>
            <img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExbWEybXJoNGgwazdmeWd5amdmbjNiaHlvbnY0YTRwZnJ2Y3N6dWYzdyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/pG9I0Qv08f0ojzYNFP/giphy.gif" width="300" />
                '''
    elif number < random_number:
        return '''
            <h1>Too low</h1>
            <img src="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExeTM5NnB4Z21qZHNlNTB0emFkZG9ybnhpcnh1ZXd5aHhtNjB2eWFuZiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9dg/2k6STSdDp2rqWXkWGL/giphy.gif" width="300" />
                '''
    else:
        return '''
            <h1>You got the correct number</h1>
            <img src="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExbGNvaTluem9pMHk1NHkwaGs1ejd1eHhtMTZjdHBrYW44NjRoYng1ayZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/VBp4n0Zn7fEKHjeUkP/giphy.gif" width="300" />
                '''


if __name__ == "__main__":
    app.run(debug=True)