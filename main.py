from flask import Flask

a = "<p>Hello, World!</p>"

app = Flask(__name__)


@app.route("/")
def hello_world():
    return a


@app.before_request
def setup():
    global a
    a = "123"


if __name__ == '__main__':
    app.run()
