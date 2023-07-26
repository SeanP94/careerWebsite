from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('FLASK_DB')
app.config['SECRET_KEY'] = os.environ.get('SC')
db = SQLAlchemy(app)

from portfolioApp import routes