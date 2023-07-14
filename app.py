from flask import Flask


app = Flask(__name__)


# Main page
@app.route("/")
def hello_world() -> str:
    return "<p>Hello, World!</p>"