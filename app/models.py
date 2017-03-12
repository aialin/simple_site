#! /usr/bin/env python
from . import db


class Author(db.Model):
    __tablename__ = 'authors'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    articles = db.relationship('Article', backref='author', lazy='dynamic')

    def __repr__(self):
        return self.name


class Article(db.Model):
    __tablename__ = "articles"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    content = db.Column(db.Text)
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'))

    def __repr__(self):
        return self.title
