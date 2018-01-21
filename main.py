from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
from decimal import *

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://reci-help:password@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)


class Ingredient(db.Model):
    __tablename__ = 'ingredient'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    price = db.Column(db.DECIMAL(4,2))

    def __init__(self, name, price):
        self.name = name
        self.price = price

class RecipeComponent(db.Model):
    __tablename__ = 'recipe_component'

    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.Integer, db.ForeignKey('ingredient.id'))
    amount = db.Column(db.Float())
    recip = db.Column(db.Integer, db.ForeignKey('recipe.id'))

        def __init__(self, item, amount, recip):
        self.item = item
        self.amount = amount
        self.recip = recip

class Recipe(db.Model):
    __tablename__ = 'recipe'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    company = db.Column(db.String(120))
    yields = db.Column(db.Integer)
    comment = db.Column(db.String(1200))

        def __init__(self, name, company, yields, comment):
        self.name = name
        self.company = company
        self.yields = yields
        self.comment = comment

@app.route('/recipes')
@app.route('/recipes/<r_id>', methods=['GET'])
def recipes():
    recipe_list = Recipe.query.all()
    r_id=request.args.get('r_id')
    if r_id:
        fetch_recipe = Recipe.query.get(r_id)
        return render_template('recipe_post.html', post=fetch_recipe)

    else:
        return render_template('recipes.html', recipe_list=recipe_list)

@app.route('/add_ingredient')  #specify price per unit
def add_ingredient():
    error_text = ''
    success_text = ''

    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        
        if name == '' or price == '':
            error_text = "Please fill out all forms"
            return render_template('add_ingredient.html', name_ph = name, price_ph = price, error_text = error_text, sucess_text = sucess_text)

        new_ingredient = Ingredient(name, price)
        db.session.add(new_ingredient)
        db.session.commit()

        ingredients = Ingredient.query.all()

        sucess_text = 'Added ' + new_ingredient + ' at $' + price + ' per unit'

    return render_template('add_ingredient.html', name_ph = '', price_ph = '', error_text = error_text, sucess_text = sucess_text))
