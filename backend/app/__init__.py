# backend/app.py
import os
from flask import Flask, jsonify
from flask_cors import CORS
from .routes import api_bp

def create_app():
    app = Flask(__name__)
    CORS(app)  # Allow Cross-Origin Resource Sharing (CORS)


    app.register_blueprint(api_bp,url_prefix='/api')

    return app
