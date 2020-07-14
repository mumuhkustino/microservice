from ims.model.user import User
from ims import response, ims, bcrypt, db
from flask import request

def login():
    try:
        email = request.json['email']
        password = request.json['password']

        user = User.query.filter_by(email=email).first()
        if not user:
            return response.bad_request([], "Empty ...")

        if not bcrypt.check_password_hash(user.password, password):
            return response.bad_request([], 'Your credentials is invalid')
        
        data = single_transform(user)
        return response.ok(data, "")
    except Exception as e:
        print(e)

def all_user():
    try:
        users = User.query.all()
        data = transform(users)
        return response.ok(data, "")
    except Exception as e:
        print(e)

def user(uid):
    try:
        user = User.query.filter_by(uid=uid).first()
        if not user:
            return response.bad_request([], 'Empty ...')
        
        data = single_transform(user)
        return response.ok(data, "")
    except Exception as e:
        print(e)

def save():
    try:
        name = request.json['name']
        email = request.json['email']
        password = request.json['password']

        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        user = User(name=name, email=email, password=hashed_password)
        db.session.add(user)
        db.session.commit()

        return response.ok('', 'Successfully save data!')
    except Exception as e:
        print(e)

def update(uid):
    try:
        name = request.json['name']
        email = request.json['email']
        password = request.json['password']

        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        user = User.query.filter_by(uid=uid).first()
        user.name = name
        user.email = email
        user.password = hashed_password
        db.session.commit()

        return response.ok('', 'Successfully save data!')
    except Exception as e:
        print(e)

def delete(uid):
    try:
        user = User.query.filter_by(uid=uid).first()
        if not user:
            return response.bad_request([], 'Empty ...')

        db.session.delete(user)
        db.session.commit()

        return response.ok('', 'Successfully delete data!')
    except Exception as e:
        print(e)

def single_transform(user, withProduct=True):
    data = {
        'uid': user.uid,
        'name': user.name,
        'email': user.email
    }
    if withProduct:
        products = []
        for product in user.products:
            products.append({
                'pid': product.pid,
                'name': product.name,
                'quantity': product.quantity
            })
        data['products'] = products

    return data

def transform(users):
    data = []
    for user in users:
        data.append(single_transform(user))
    return data