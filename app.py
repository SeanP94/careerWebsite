from flask import Flask, render_template
#export FLASK_APP=app.py ; export FLASK_ENV=development ;flask run
#export FLASK_DB=sqlite:///test.db
app = Flask(__name__)


# Main page
@app.route("/")
@app.route("/home")
def homePage() :
    return render_template('home.html', pageTitle='Home Page')


@app.route("/resume")
def resume_page():
    return render_template('resume.html')