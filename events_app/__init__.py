"""Import packages and modules for initializing our app."""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from events_app.config import Config

app = Flask(__name__)
app.config.from_object(Config)


SECRET_KEY = os.getenv("SECRET_KEY")
db = SQLAlchemy(app)

from events_app.main.routes import main

app.register_blueprint(main)

with app.app_context():
    db.create_all()
