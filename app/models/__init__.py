from flask import Flask


def init_app(app: Flask):
    # Importanto a função home_view() e passando o app por parâmetro
    from app.models.posts_model import Post
    Post(app)

    return app
