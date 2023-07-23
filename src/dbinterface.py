import os
import sqlalchemy as sa
from datetime import datetime

#export FLASK_DB=sqlite:///test.db

metadata = sa.MetaData()
# Create a table to learn with
first = sa.Table(
    'first', metadata,
    sa.Column('first_id', sa.Integer(), primary_key=True),
    sa.Column('name', sa.String(50), index=True),
    sa.Column('age', sa.Integer()),
    sa.Column('date', sa.DateTime(), default=datetime.now)
)

engine = sa.create_engine(os.environ.get('FLASK_DB'))

conn = engine.connect()
metadata.create_all(engine) # Will create any tables that do not exist.

# Always close connection
conn.close()