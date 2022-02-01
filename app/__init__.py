from flask import Flask
from app.controllers import products_controller


def create_app():

    app = Flask(__name__)

    products_controller.init_app(app)

    return app
