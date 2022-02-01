from pymongo import MongoClient
from datetime import datetime


client = MongoClient('mongodb://localhost:27017/')

db = client['TestTec']


class Products():

    def __init__(self, name, price, content):
        self.create_at = datetime.now().strftime('%d/%m/%Y')
        self.name = name
        self.price = price
        self.content = content

    def validate(**kwargs):
        required_keys = ['name', 'price', 'content']

        for key in required_keys:
            if key not in kwargs:
                raise KeyError(f'{key} Not found')

    @staticmethod
    def get_all():

        products_list = list(db.TestTec.find())
        # db.products.remove()

        for product in products_list:
            del product['_id']

        return products_list

    @staticmethod
    def get_product_by_id(id):
        product = db.TestTec.find_one({'id': id})

        try:
            del product['_id']
            return product
        except:
            return {'Error': 'product not found'}, 404

    def save(self):
        products_list = Products.get_all()

        if len(products_list) == 0:
            self.__dict__['id'] = len(products_list)+1
        else:
            self.__dict__['id'] = products_list[-1]['id'] + 1

        _id = db.TestTec.insert_one(self.__dict__).inserted_id

        new_products = db.TestTec.find_one({'_id': _id})

        del new_products['_id']

        return new_products

    @staticmethod
    def delete(id):
        products = db.TestTec.find_one({'id': id})

        try:
            del products['_id']
            db.TestTec.delete_one(products)
            return products
        except:
            return {'Error': 'products not found'}, 404

    def update(self, id):
        products = db.TestTec.find_one({'id': id})

        try:
            update = {
                "$set": {
                    "id": id,
                    "name": self.name,
                    "price": self.price,
                    "content": self.content,
                    "updated_at": datetime.now().strftime('%d/%m/%Y')
                }
            }
            db.TestTec.update_one(products, update)
            products_update = Products.get_product_by_id(id)
            return products_update
        except:
            if not products:
                return{'error': 'post not found'}, 404
