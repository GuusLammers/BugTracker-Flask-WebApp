from . import db
from datetime import datetime
from flask_login import UserMixin


# user database model
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    projects = db.relationship('Project', backref='owner')


# project database model
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(1000), nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    state = db.Column(db.String(100), nullable=False, default='Active')
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    due_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    tickets = db.relationship('Ticket', backref='project')


# ticket database model
class Ticket(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(1000), nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    due_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    priority = db.Column(db.String(50), nullable=False)
    state = db.Column(db.String(100), nullable=False, default='Open')
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'))
