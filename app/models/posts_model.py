from pymongo import MongoClient
from datetime import date, datetime


client = MongoClient('mongodb://localhost:27017/')

db = client['kenzie']


class Post():

    def __init__(self, title, author, tags, content):
        self.create_at = datetime.now().strftime('%d/%m/%Y')
        self.title = title
        self.author = author
        self.tags = tags
        self.content = content

    def validate(**kwargs):
        required_keys = ['title', 'author', 'tags', 'content']

        for key in required_keys:
            if key not in kwargs:
                raise KeyError(f'{key} Not found')

    @staticmethod
    def get_all():

        posts_list = list(db.posts.find())
        # db.posts.remove()

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

    def save(self):
        users_list = Post.get_all()

        if len(users_list) == 0:
            self.__dict__['id'] = len(users_list)+1
        else:
            self.__dict__['id'] = users_list[-1]['id'] + 1

        _id = db.posts.insert_one(self.__dict__).inserted_id

        new_post = db.posts.find_one({'_id': _id})

        del new_post['_id']

        print(new_post)

        return new_post

    @staticmethod
    def delete(id):
        post = db.posts.find_one({'id': id})

        try:
            del post['_id']
            db.posts.delete_one(post)
            return post
        except:
            return {'Error': 'Post not found'}, 404

    def update(self, id):
        post = db.posts.find_one({'id': id})

        try:
            update = {
                "$set": {
                    "id": id,
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
