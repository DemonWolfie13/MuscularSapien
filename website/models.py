from . import db
from sqlalchemy.sql import func

class Note(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    username = db.Column(db.String(20), unique=True,nullable=False)
    email = db.Column(db.String(120), unique=True,nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(20),nullable=False)
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())
    notes = db.relationship('Note')

    def __repr__(self):
        return f'{self.username} : {self.email} : {self.date_created}'

