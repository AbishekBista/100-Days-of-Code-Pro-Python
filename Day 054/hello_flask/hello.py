from flask import Flask

app = Flask(__name__)

print(__name__)

@app.route('/')
def hello_world():
    return 'Hello, world!'

@app.route('/mario')
def hello_abishek():
    return 'Hello, Mario!'

if __name__ == '__main__':
    app.run()