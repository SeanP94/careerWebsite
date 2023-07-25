
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

#export FLASK_DB=sqlite:///test.db
#https://stackoverflow.com/questions/9692962/flask-sqlalchemy-import-context-issue/9695045#9695045

# Will be Initialized later in app.py
db = SQLAlchemy()


class FirstTable(db.Model):
    first_id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=50))
    age = db.Column(db.Integer())
    date = db.Column(db.DateTime(), default=datetime.now)

    def __repr__(self):
        return f'{self.first_id} : {self.name} : {self.age} : {self.date}'

# metadata = sa.MetaData()
# # Create a table to learn with
# first = sa.Table(
#     'first', metadata,
#     sa.Column('first_id', sa.Integer(), primary_key=True),
#     sa.Column('name', sa.String(50), index=True),
#     sa.Column('age', sa.Integer()),
#     sa.Column('date', sa.DateTime(), default=datetime.now)
# )

# engine = sa.create_engine(os.environ.get('FLASK_DB'))

# conn = engine.connect()
# metadata.create_all(engine) # Will create any tables that do not exist.

# # Always close connection
# conn.close()