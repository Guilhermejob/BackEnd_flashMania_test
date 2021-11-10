from flask import Flask


def init_app(app: Flask):
    # Importanto a função home_view() e passando o app por parâmetro
    from app.controllers.posts_controller import init_app
    init_app(app)

    return app
