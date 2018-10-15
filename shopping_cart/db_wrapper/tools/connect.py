import logging.config

import psycopg2

log = logging.getLogger()


def get_credentials(**params):
    if not params:
        raise ValueError("'params' is empty or None")

    keys = "database, user, DB_PASWWORD,DB_HOST"
    if not all(items for items in params.values()):
        raise ValueError(
            "Missing DB Credentials. Check settings.ini file and "
            f"configure the {keys}")

    else:
        return params


def connect(**credentials):
    # connect to the PostgreSQL server
    log.info('Connecting to the PostgreSQL database...')
    try:
        conn = psycopg2.connect(**credentials)

        if conn.closed != 0:
            raise Exception("Restart postgresql service")

        return conn

    # Raises psycopg2.ProgrammingError, psycopg2.OperationalError
    except Exception:
        raise


def execute_sql(conn, sql):
    # try:
    cursor = conn.cursor()

    # Execute SQL
    cursor.execute(sql)

    return cursor

    # except:
    #     conn.rollback()

    # finally:
    #     conn.commit()
