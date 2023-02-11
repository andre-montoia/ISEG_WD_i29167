from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Create the Flask app
app = Flask(__name__)

# Configure the app
app.config.from_pyfile('config.py')

# Initialize the SQLAlchemy database
db = SQLAlchemy(app)

# Import the routes and models modules
from app import routes, models