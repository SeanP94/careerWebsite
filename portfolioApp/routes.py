from portfolioApp import app
from flask import render_template
from portfolioApp.models import FirstTable
import portfolioApp.forms as forms

@app.route("/")
@app.route("/home")
def homePage() :
    return render_template('homepage.html', pageTitle='Home Page')


@app.route("/resume")
def resume_page():
    return render_template('resume.html')

@app.route("/login")
def login_page():
    form = forms.LoginUser()

    return render_template('login.html', form=form)

@app.route("/createuser")
def register_page():
    form = forms.CreateUser()

    return render_template('createuser.html', form=form)