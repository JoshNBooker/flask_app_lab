from app import db

class Meal(db.Model):
    __tablename__ = 'meals'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    recipes = db.relationship('Recipe', backref='meal')

class Recipe(db.Model):
    __tablename__ = 'recipes'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    ingredients = db.Column(db.String(200))
    time = db.Column(db.Integer)
    method = db.Column(db.String(200))
    meal_id = db.Column(db.Integer, db.ForeignKey('meals.id'))
