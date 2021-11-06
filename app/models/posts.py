from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

db = client['kenzie']


class Post():

    def __init__(self, id: int, create_at: str, update_at: str, title: str, author: str, tags: list = [], content: str = ''):
        self.id = id
        self.create_at = create_at
        self.update_at = update_at
        self.title = title
        self.author = author
        self.tags = tags
        self.content = content

    @staticmethod
    def get_all():
        posts_list = list(db.posts.find())
        return posts_list
