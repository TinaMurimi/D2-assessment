import os

from decouple import config

APP_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
ROOT_DIR = os.path.abspath(os.path.dirname(APP_DIR))

DEBUG = config('DEBUG', default=False)
SECRET_KEY = config('SECRET_KEY', default=False)

DB_SETTINGS = {
    'database': config('DB_NAME'),
    'user': config('DB_USER'),
    'password': config('DB_PASWWORD'),
    'host': config('DB_HOST', 'localhost'),
    'port': config('DB_HOST', 5432),
}
