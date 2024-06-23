from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    
    # Load environment variables
    load_dotenv()
    
    # Configure the SQLAlchemy part of the app instance
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Initialize the app with the extension
    db.init_app(app)
    migrate.init_app(app, db)
    
    # Import and register the blueprints
    from .authentication import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    
    return app
