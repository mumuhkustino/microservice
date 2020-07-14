from ims import ims
from ims.controller import user_controller, product_controller
from flask import request

@ims.route('/')
@ims.route('/home')
def home():
    return "Hello, World!"

@ims.route('/register', methods=['POST'])
def register():
    return user_controller.save()

@ims.route('/login', methods=['POST'])
def login():
    return user_controller.login()

@ims.route('/users', methods=['GET'])
def users():
    return user_controller.all_user()
        

@ims.route('/users/<uid>', methods=['PUT', 'GET', 'DELETE'])
def user(uid):
    if request.method == 'GET':
        return user_controller.user(uid)
    elif request.method == 'PUT':
        return user_controller.update(uid)
    elif request.method == 'DELETE':
        return user_controller.delete(uid)

@ims.route('/products', methods=['POST', 'GET'])
def products():
    if request.method == 'GET':
        return product_controller.all_product()
    else:
        return product_controller.save()

@ims.route('/products/<pid>', methods=['PUT', 'GET', 'DELETE'])
def product(pid):
    if request.method == 'GET':
        return product_controller.product(pid)
    elif request.method == 'PUT':
        return product_controller.update(pid)
    elif request.method == 'DELETE':
        return product_controller.delete(pid)