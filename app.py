from flask import Flask, render_template
#export FLASK_APP=app.py ; export FLASK_ENV=development ;flask run
#export FLASK_DB=sqlite:///test.db
app = Flask(__name__)


# Main page
@app.route("/")
def homePage_() :
    return render_template('homepage.html')

@app.route("/home")
def homePage() :
    return render_template('generic.html', pageTitle='MainPage')


@app.route("/resume")
def resume_page():
    return render_template('resume.html')