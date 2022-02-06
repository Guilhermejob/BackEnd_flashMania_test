from flask import Flask, jsonify, request, send_file
from app.exceptions.products_exceptions import TypeNotAllowedError
from app.models.products_model import Products
from flask_cors import CORS
from werkzeug.datastructures import ImmutableMultiDict
import ipdb

import io


def init_app(app: Flask):
    CORS(app)

    # Função que lista todos os produtos
    @app.get('/products')
    def get_all_products():

        products_list = Products.get_all()
        return jsonify([{
            "name": product['name'],
            "price":product['price'],
            "id": product['id'],
            'img_url': f'http://127.0.0.1:5000/products/img/{product["id"]}'
        }for product in products_list

        ])

    # Função responsavel por pegar a imagem do produto
    @app.get('/products/img/<int:id>')
    def get_product_by_id_img(id: int):
        product = Products.get_product_by_id(id)
        return send_file(io.BytesIO(product['img']),  attachment_filename=product['img_name'])

    # Função para pegar um item especifico usando o id como referencia
    @app.get('/products/<int:id>')
    def get_product_by_id(id: int):
        product = Products.get_product_by_id(id)
        return_product = {
            "name": product['name'],
            "id": product['id'],
            'price': product['price'],
            'img_url': f'http://127.0.0.1:5000/products/img/{product["id"]}'
        }
        return jsonify(return_product)

    # Função para cadastrar os dados do produto
    @app.post('/products')
    def create_product():
        data = request.form.to_dict()

        img = request.files['img']

        img_filename = img.filename

        if img:
            img = img.read()

        data['img'] = img

        data['img_name'] = img_filename

        data['price'] = float(data['price'])

        print('-' * 15, data, '-' * 15)

        try:
            name = data['name']
            price = data['price']
            content = data['content']

            try:
                if type(name) != str or type(price) != float or type(content) != str:
                    raise TypeNotAllowedError(name, price, content)

                product = Products(**data)
                created_product = product.save()

                return jsonify({'name': created_product['name'], 'price': created_product['price'], "id": created_product['id'], "img_name": created_product['img_name']}), 201

            except TypeNotAllowedError as err:
                print(err.message)
                return err.message, 400

        except KeyError as err:
            return {'error': f'Missing key {err}'}, 400

    # Função responsavel por atualizar o produto
    @ app.patch('/products/<int:id>')
    def update_product(id: int):
        data = request.form.to_dict()

        img = request.files['img']

        img_filename = img.filename

        if img:
            img = img.read()

        data['img'] = img

        data['img_name'] = img_filename

        data['price'] = float(data['price'])

        try:
            name = data['name']
            price = data['price']
            content = data['content']

            try:
                if type(name) != str or type(price) != float or type(content) != str:
                    raise TypeNotAllowedError(name, price, content)
                product = Products(**data)
                product.__dict__['id'] = id
                update_product = product.update(id)
                return jsonify({'name': update_product['name'], 'price': update_product['price'], "id": update_product['id'], "img_name": update_product['img_name']}), 200
            except TypeNotAllowedError as err:
                return err.message, 400

        except KeyError as err:
            return {'error': f'Missing key {err}'}, 400

    @app.delete('/products/<int:id>')
    def delete_product(id: int):
        product = Products.delete(id)
        return jsonify({'msg': 'Produdo Deletado com sucesso'})
