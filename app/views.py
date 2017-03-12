from . import app, db
from flask import render_template, request
from .models import Author, Article

@app.route('/')
def index():
    author_lst = Author.query.all()
    string = ''
    for author in author_lst:
        string += 'author:' + author.name
        for i, article in enumerate(author.articles, 1):
            string += str(i) + '.' + article.title
    return render_template('index.html', authors=author_lst)
