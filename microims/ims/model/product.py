from ims import db
from datetime import datetime
from ims.model.user import User

class Product(db.Model):
    pid = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    name = db.Column(db.String(200), nullable=False)
    quantity = db.Column(db.Integer, nullable=False, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.BigInteger, db.ForeignKey(User.uid))
    users = db.relationship("User", backref="user_id")

    def __repr__(self):
        return '<Product {}>'.format(self.name)