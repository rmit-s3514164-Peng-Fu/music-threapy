from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
# DB Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('postgres://mvhctbhnyjqbph:gCuRtzxvVNUycilGrDD2GIFjv9@ec2-54-235-78-240.compute-1.amazonaws.com:5432/d1tbu4993m5g5p')
db = SQLAlchemy(app)


from app import views
