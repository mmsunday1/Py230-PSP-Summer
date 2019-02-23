from datetime import datetime
from model import db, User, Task
from passlib.hash import pbkdf2_sha256

db.connect()
db.drop_tables([User, Task])
db.create_tables([User, Task])

Task(name="Do the Laundry.").save()
Task(name="Do the dishes.", performed=datetime.now()).save()
User(name="admin", password=pbkdf2_sha256.hash("password")).save()
User(name="bob", password=pbkdf2_sha256.hash("bobbob")).save()
