from flask import Flask, render_template
#export FLASK_APP=app.py ; export FLASK_ENV=development ;flask run

app = Flask(__name__)


# Main page
@app.route("/")
def homePage() :
    return render_template('homepage.html')

@app.route("/resume")
def resume_page():
    return render_template('resume.html')