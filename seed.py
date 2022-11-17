from peewee import *
from models import db, Note

db.connect()
db.drop_tables([Note])
db.create_tables([Note])


Note(title="Update Portfolio", message="Add contact form").save()