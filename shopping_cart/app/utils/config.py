import os

from decouple import config

APP_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
ROOT_DIR = os.path.abspath(os.path.dirname(APP_DIR))

DEBUG = config('DEBUG', default=False)
SECRET_KEY = config('SECRET_KEY', default=False)

POSTGRES = {
    'dbuser': config('DB_USER'),
    'dbpass': config('DB_PASWWORD'),
    'dbname': config('DB_NAME'),
    'dbhost': 'localhost',
    'dbport': '5432',
}
