import os
from flask import Flask
from .app.routes import api_blueprint
from src.app.config.db import db
from src.app.config.ma import ma
from dotenv import load_dotenv
from flask_marshmallow import Marshmallow

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_DATABASE')}"
db.init_app(app)
ma.init_app(app)
app.register_blueprint(api_blueprint)
