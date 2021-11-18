from flask import Flask, jsonify, request
from app.exceptions.posts_exceptions import TypeNotAllowedError
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
        data = request.json

        try:
            title = data['title']
            author = data['author']
            tags = data['tags']
            content = data['content']

            try:
                if type(title) != str or type(author) != str or type(tags) != list or type(content) != str:
                    raise TypeNotAllowedError(title, author, tags, content)
                post = Post(**data)
                created_post = post.save()
                return created_post

            except TypeNotAllowedError as err:
                print(err.message)
                return err.message, 400

        except KeyError as err:
            return {'error': f'Missing key {err}'}, 400

    @app.delete('/posts/<int:id>')
    def delete_post(id: int):
        post = Post.delete(id)
        return post

    @app.patch('/posts/<int:id>')
    def update_post(id: int):
        data = request.json

        try:
            title = data['title']
            author = data['author']
            tags = data['tags']
            content = data['content']

            try:
                if type(title) != str or type(author) != str or type(tags) != list or type(content) != str:
                    raise TypeNotAllowedError(title, author, tags, content)
                post = Post(**data)
                post.__dict__['id'] = id
                update_post = post.update(id)
                return update_post
            except TypeNotAllowedError as err:
                return err.message, 400

        except KeyError as err:
            return {'error': f'Missing key {err}'}, 400
