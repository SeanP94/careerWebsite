from portfolioApp import app
from flask import render_template
from portfolioApp.models import FirstTable

@app.route("/")
@app.route("/home")
def homePage() :
    return render_template('homepage.html', pageTitle='Home Page')


@app.route("/resume")
def resume_page():
    return render_template('resume.html')

@app.route("/login")
def login_page():
    return render_template('login.html')