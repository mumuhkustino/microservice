from ims import db
from datetime import datetime

class User(db.Model):
    uid = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(100), index=True, unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)
    products = db.relationship("Product", lazy="select", backref=db.backref('products', lazy='joined'))

    def __repr__(self):
        return '<User {}>'.format(self.name)