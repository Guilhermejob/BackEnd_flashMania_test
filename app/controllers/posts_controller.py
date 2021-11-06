from flask import Flask, jsonify
from app.models.posts import Post


def init_app(app: Flask):

    @app.get('/posts')
    def get_all_posts():
        users_list = Post.get_all()
        return jsonify(users_list)
