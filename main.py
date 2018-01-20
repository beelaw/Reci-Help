from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
from decimal import *

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://reci-help:password@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

class ReciList

class Ingredient(db.Model):
    __tablename__ = 'ingredient'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    price = db.Column(db.DECIMAL(4,2))

    def __init__(self, title, body):
        self.name = name
        self.price = price

class RecipeComponent(db.Model):
    __tablename__ = 'recipe_component'

    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.Integer, db.ForeignKey('ingredient.id'))
    amount = db.Column(db.Float())

class Recipe(db.Model): #company name and yield
    __tablename__ = 'recipe'
