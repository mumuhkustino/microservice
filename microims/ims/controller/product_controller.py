from ims.model.product import Product
from flask import request, jsonify
from ims import response, db
from ims.controller import user_controller

def all_product():
    try:
        user_id = request.args.get('user_id')
        product = Product.query.filter_by(user_id=user_id).all()
        data = transform(product)
        return response.ok(data, "")
    except Exception as e:
        print(e)

def save():
    try:
        name = request.json['name']
        quantity = request.json['quantity']
        user_id = request.json['user_id']
        
        product = Product(name=name, user_id=user_id)
        if request.json['quantity']:
            product.quantity = request.json['quantity']
        db.session.add(product)
        db.session.commit()
        return response.ok('', 'Successfully save data!')
    except Exception as e:
        print(e)

def update(pid):
    try:
        name = request.json['name']
        quantity = request.json['quantity']
        product = Product.quey.filter_by(pid=pid).first()
        product.name = name
        product.quantity = quantity

        db.session.commit()
        return response.ok('', 'Successfully update product!')
    except Exception as e:
        print(e)

def product(pid):
    try:
        product = Product.query.filter_by(pid=pid).first()
        if not product:
            return response.bad_request([], 'Empty ...')

        data = single_transform(product)
        return response.ok(data, "")
    except Exception as e:
        print(e)
        
def delete(pid):
    try:
        product = Product.query.filter_by(pid=pid).first()
        if not product:
            return response.bad_request([], 'Empty ...')

        db.session.delete(product)
        db.session.commit()

        return response.ok('', 'Successfully delete product!')
    except Exception as e:
        print(e)

def transform(products):
    data = []
    for product in products:
        data.append(single_transform(product))
    return data

def single_transform(product):
    data = {
        'pid': product.pid,
        'name': product.name,
        'quantity': product.quantity,
        'created_at': product.created_at,
        'updated_at': product.updated_at,
        'user_id': product.user_id,
        'user': user_controller.single_transform(product.users, withProduct=False)
    }
    return data