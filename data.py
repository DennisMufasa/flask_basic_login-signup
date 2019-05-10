from peewee import *

db = SqliteDatabase('users.db')

class User(Model):
    username = TextField()
    password = TextField()
    email = TextField()

    class Meta:
        database = db

# User.create_table()

