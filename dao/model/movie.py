from setup_db import db
from marshmallow import Schema, fields


"""Модель фильма и схема сериализации"""
class Movie(db.Model):
    __tablename__ = 'movie'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    descriptions = db.Column(db.String)
    trailer = db.Column(db.String)
    year = db.Column(db.Integer)
    rating = db.Column(db.Float)
    genre_id = db.Column(db.Integer, db.ForeignKey("genre.id"))
    genre = db.relationship("Genre")  #??????????
    director_id = db.Column(db.Integer, db.ForeignKey("director.id"))
    director = db.relationship("Director")  #??????????

