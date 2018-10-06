import datetime

import flask
from flask_restful import Api
from flask_sqlalchemy import Model, SQLAlchemy

from app.utils import config

from app.views.shoppers import ShopperAPI
from app.models import db

app = flask.Flask(__name__, instance_relative_config=True)
app.config["DEBUG"] = config.DEBUG
app.config['SECRET_KEY'] = config.SECRET_KEY

database_uri = 'postgresql+psycopg2://{dbuser}:{dbpass}@{dbhost}:{dbport}/{dbname}'.format(
    **config.POSTGRES)

print(f"\ndatabase_uri: {database_uri}\n")

app.config.update(
    SQLALCHEMY_DATABASE_URI=database_uri,
    # Silence the deprecation warning
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
)

# Bind db to app
db.init_app(app)

# Register resources
api = Api(app)
api.add_resource(ShopperAPI,
                 '/shopping_cart/v1.0/auth/register',
                 endpoint='register_user')
