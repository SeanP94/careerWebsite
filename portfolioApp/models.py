from portfolioApp import db 
from datetime import datetime


class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=60), nullable=False)

class FirstTable(db.Model):
    first_id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=50))
    age = db.Column(db.Integer())
    date = db.Column(db.DateTime(), default=datetime.now)

    def __repr__(self):
        return f'{self.first_id} : {self.name} : {self.age} : {self.date}'
