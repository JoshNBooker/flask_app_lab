from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://josh@localhost:5432/recipes_app"

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from controller.recipes_controller import recipes_blueprint

app.register_blueprint(recipes_blueprint)

