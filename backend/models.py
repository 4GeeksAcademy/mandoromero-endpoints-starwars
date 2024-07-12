from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.hybrid import hybrid_property
from flask import Flask, request, jsonify, url_for, Blueprint
from backend.models import db, User
from flask_cors import CORS


db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "User"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(
        db.String(64),
        
    )
    email = db.Column(
    db.String(120), 
    unique=True, 
    nullable=False
    )
    photos = db.relationship(
    "backend.models.photo",
    back_populates = "user",
    uselist = True,
    is_active = db.Column(db.Boolean, default = True)
    )
    is_active = db.Column(
    db.Boolean(),
    unique=False, 
    nullable=False
    )

    def __repr__(self) -> str:
        return f"<User {self.username}>"

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # Do not serialize the password, it's a security breach
        }

class People(db.Model):
    __tablename__ = "people"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    age = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<People {self.name}>'

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age
        }

class Planets(db.Model):
    __tablename__ = "planets"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    population = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Planets {self.name}>'

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "population": self.population
        }
