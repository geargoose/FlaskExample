from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


def main(*args, **kwargs):
    app.run(*args, **kwargs)


if __name__ == '__main__':
    main()
