from datetime import datetime
from mongoengine import Document, StringField, DateTimeField, EmailField

class User(Document):
    firstName = StringField(max_length=20, required=True)
    lastName = StringField(max_length=20, required=True)
    email = EmailField(max_length=120, unique=True, required=True)
    password = StringField(required=True)
    maritalStatus = StringField(max_length=50)
    country = StringField(max_length=50)
    created_at = DateTimeField(default=datetime.utcnow())
