from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('FLASK_DB')
db = SQLAlchemy(app)

from portfolioApp import routes