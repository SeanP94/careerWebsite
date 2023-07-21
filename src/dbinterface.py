import os
from sqlalchemy import create_engine, text

engine = create_engine(os.environ.get('FLASK_DB'))

with engine.connect() as connection:
    result = connection.execute(text('SELECT "HELLO"'))
    print(result.all())