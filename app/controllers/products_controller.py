from tokenize import Number
from unicodedata import numeric
from flask import Flask, jsonify, request
from jinja2 import Undefined
from app.exceptions.products_exceptions import TypeNotAllowedError
from app.models.products_model import Products


def init_app(app: Flask):

    @app.get('/products')
    def get_all_products():

        products_list = Products.get_all()
        return jsonify(products_list)

    @app.get('/products/<int:id>')
    def get_product_by_id(id: int):
        product = Products.get_product_by_id(id)
        return product

    @app.post('/products')
    def create_product():
        data = request.json

        try:
            name = data['name']
            price = data['price']
            content = data['content']

            try:
                if type(name) != str or type(price) != float or type(content) != str:
                    raise TypeNotAllowedError(name, price, content)
                product = Products(**data)
                created_product = product.save()
                return created_product

            except TypeNotAllowedError as err:
                print(err.message)
                return err.message, 400

        except KeyError as err:
            return {'error': f'Missing key {err}'}, 400

    @app.delete('/products/<int:id>')
    def delete_product(id: int):
        product = Products.delete(id)
        return product

    @app.patch('/products/<int:id>')
    def update_product(id: int):
        data = request.json

        try:
            name = data['name'] or Undefined
            price = data['price'] or Undefined
            content = data['content'] or Undefined

            try:
                if type(name) != str or type(price) != float or type(content) != str:
                    raise TypeNotAllowedError(name, price, content)
                product = Products(**data)
                product.__dict__['id'] = id
                update_product = product.update(id)
                return update_product, 201
            except TypeNotAllowedError as err:
                return err.message, 400

        except KeyError as err:
            return {'error': f'Missing key {err}'}, 400
