from flask import Flask

a = "<p>Hello, World!</p>"

app = Flask(__name__)


@app.route("/")
def hello_world():
    return a


if __name__ == '__main__':
    a = "<p>Hello, Egor!</p>"
    app.run()
