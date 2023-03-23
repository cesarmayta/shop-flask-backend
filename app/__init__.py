from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager

from .blueprints.shop import shop #Aquí importamos el blueprint
from .blueprints.auth import auth

from .config import Config

def create_app():

    app = Flask(__name__)
    
    CORS(app)
    app.config.from_object(Config)
    jwt = JWTManager(app)

    app.register_blueprint(shop)
    app.register_blueprint(auth)

    return app