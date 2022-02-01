from flask import Flask


def init_app(app: Flask):
    from app.controllers.products_controller import init_app
    init_app(app)

    return app
