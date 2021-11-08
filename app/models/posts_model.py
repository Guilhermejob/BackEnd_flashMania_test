from pymongo import MongoClient
from datetime import date, datetime

from pymongo.message import update

from app.exceptions.posts_exceptions import InvalidPostError

client = MongoClient('mongodb://localhost:27017/')

db = client['kenzie']


class Post():

    def __init__(self, title: str, author: str, tags: list = [], content: str = ''):
        self.create_at = datetime.now().strftime('%d/%m/%Y')
        self.title = title
        self.author = author
        self.tags = tags
        self.content = content

    def validate(**kwargs):
        required_keys = ['id', 'title', 'author', 'tags', 'content']

        for key in required_keys:
            if key not in kwargs:
                raise KeyError(f'{key} Not found')

    @staticmethod
    def get_all():

        posts_list = list(db.posts.find())

        for post in posts_list:
            del post['_id']

        return posts_list

    @staticmethod
    def get_post_by_id(id):
        post = db.posts.find_one({'id': id})

        try:
            del post['_id']
            return post
        except:
            return {'Error': 'Post not found'}, 404

        return post

    def save(self):
        _id = db.posts.insert_one(self.__dict__).inserted_id

        if not _id:
            raise InvalidPostError

        new_post = db.posts.find_one({'_id': _id})

        del new_post['_id']

        return new_post

    @staticmethod
    def delete(id):
        posts_list = list(db.posts.find())

        for post in posts_list:

            del post['_id']

            if post['id'] == id:
                post_filtered = post

        db.posts.delete_one(post_filtered)

        return post_filtered, 200

    def update(self, id):
        post = db.posts.find_one({'id': id})

        try:
            update = {
                "$set": {
                    "title": self.title,
                    "author": self.author,
                    "tags": self.tags,
                    "content": self.content,
                    "updated_at": datetime.now().strftime('%d/%m/%Y')
                }
            }
            db.posts.update_one(post, update)
            post_update = Post.get_post_by_id(id)
            return post_update
        except:
            if not post:
                return{'error': 'post not found'}, 404
