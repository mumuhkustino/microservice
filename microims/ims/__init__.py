from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt

ims = Flask(__name__)
ims.config.from_object(Config)
db = SQLAlchemy(ims)
migrate = Migrate(ims, db)
bcrypt = Bcrypt(ims)

from ims.model import user, product
from ims import routes