from decouple import config

DB_SETTINGS = {
    'database': config('DB_NAME'),
    'user': config('DB_USER'),
    'password': config('DB_PASWWORD'),
    'host': config('DB_HOST', 'localhost'),
}
