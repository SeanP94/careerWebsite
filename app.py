from flask import Flask, render_template
#export FLASK_APP=app.py ; export FLASK_ENV=development ;flask run

app = Flask(__name__)


# Main page
@app.route("/")
def hello_world() :
    return render_template('homepage.html')