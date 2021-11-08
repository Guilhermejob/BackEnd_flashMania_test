from flask import Flask, jsonify, request
from app.exceptions.posts_exceptions import InvalidPostError
from app.models.posts_model import Post


def init_app(app: Flask):

    @app.get('/posts')
    def get_all_posts():
        users_list = Post.get_all()
        return jsonify(users_list)

    @app.get('/posts/<int:id>')
    def get_post_by_id(id: int):
        post = Post.get_post_by_id(id)
        return post

    @app.post('/posts')
    def create_post():
        users_list = Post.get_all()

        data = request.json
        data['id'] = len(users_list)

        try:
            Post.validate(**data)
            post = Post(**data)
            new_post = post.save()
            return new_post, 201

        except (InvalidPostError):
            return {'Message': 'Dados invalidos para a criação de um post'}, 400
