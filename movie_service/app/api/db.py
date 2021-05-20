'''
Here, DATABASE_URI is the URL used to connect to the PostgreSQL 
database. Here movie_user is the name of the database user, 
movie_password is the password of the database user and 
movie_db is the name of the database.

Just like you would to in SQLAlchemy you have created the 
table for the movies database.
'''

from sqlalchemy import (Column, Integer, MetaData, String, Table,
                        create_engine, ARRAY)

from databases import Database

DATABASE_URL = 'postgresql://postgres:MisterMonkey8@localhost/movie_db'

engine = create_engine(DATABASE_URL)
metadata = MetaData()

movies = Table(
    'movies',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(50)),
    Column('plot', String(250)),
    Column('genres', ARRAY(String)),
    Column('casts', ARRAY(String))
)

database = Database(DATABASE_URL)