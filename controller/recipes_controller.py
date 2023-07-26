from flask import Flask, render_template, redirect, Blueprint, request
from app import db
from models import Meal, Recipe

recipes_blueprint = Blueprint('recipes',__name__)

@recipes_blueprint.route("/")
def home():
    return "This is the home page!"

# db.session.commit()
# return 