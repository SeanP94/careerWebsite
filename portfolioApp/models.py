from portfolioApp import db
from datetime import datetime

class FirstTable(db.Model):
    first_id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=50))
    age = db.Column(db.Integer())
    date = db.Column(db.DateTime(), default=datetime.now)

    def __repr__(self):
        return f'{self.first_id} : {self.name} : {self.age} : {self.date}'
