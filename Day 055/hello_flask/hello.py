from flask import Flask

app = Flask(__name__)

def make_bold(function):
    def wrapper_function():
        return f'<b>{function()}</b>'
    return wrapper_function

def make_italic(function):
    def wrapper_function():
        return f'<em>{function()}</em>'
    return wrapper_function

def make_underlined(function):
    def wrapper_function():
        return f'<u>{function()}</u>'
    return wrapper_function

@app.route('/')
def say_hello():
    return '''
        <h1 style="color: red">Hello, there!</h1>
        <p>This is a paragraph</p>
        <img src="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExcWkybzk1eTY1NGlwa3ZqcDM1YnRiOWl5MHRiMmxid2N4ZW1wMWRjZSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/vFKqnCdLPNOKc/giphy.gif" width="200" />
            '''

@app.route('/bye')
@make_bold
@make_italic
@make_underlined
def  bye():
    return 'Bye'

@app.route('/username/<name>')
def greet(name):
    return f"Hello {name}"

@app.route('/details/<name>/<int:age>')
def greet_with_age(name, age):
    return f"Hello {name}, you are {age} years old."

# Advanced python decorators with args and kwargs

def is_authenticated_decorator(function):
    def wrapper_function(*args):
        if args[0].is_logged_in == True:
            function(args[0])
    return wrapper_function


class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False

@is_authenticated_decorator
def createUserBlog(user):
    print(f"This is {user.name}'s blog.")

new_user = User("Mario")
new_user.is_logged_in = True
createUserBlog(new_user)

if __name__ == "__main__":
    app.run(debug=True)