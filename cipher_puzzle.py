from flask import Flask
app = Flask(__name__)


@app.route("/")
@app.route("/cipher")
def home():
    return "<h1>Cipher Puzzle</h1>"


if __name__ == '__main__':
    app.run(debug=True)
