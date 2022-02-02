from flask import Flask

a = "<p>Hello, World!</p>"

app = Flask(__name__)


@app.route("/")
def hello_world():
    return a


def main(*args, **kwargs):
    global a
    a = "<p>Hello, Egor!</p>"
    app.run(*args, **kwargs)


if __name__ == '__main__':
    main()
