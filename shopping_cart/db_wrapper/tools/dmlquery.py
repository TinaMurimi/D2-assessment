import logging.config
import os

import psycopg2

from .wrapper import DBWrapper
from .params_parser import ParseParameters

from app.utils import config


class DMLQuery(DBWrapper):
    def __init__(self, connection):
        super().__init__()

        # Set up logger
        logging.config.fileConfig(os.path.join(
            config.ROOT_DIR, "logging.ini"))
        self.logger = logging.getLogger()

        # DB connection
        self.conn = connection
        if not self.conn:
            raise ValueError("No DB connection provided")

    def execute_sql(self, sql, params=None):
        try:
            cursor = self.conn.cursor()

            # Execute SQL
            cursor.execute(sql)

            # Commit the changes to the database
            self.conn.commit()

            return cursor

        except (Exception, psycopg2.DatabaseError) as error:
            raise

        # finally:
        #     if self.conn is not None:
        #         self.conn.close()

    def create(self, table, params):
        """
        Insert a new record in a DB table

        parameter
        params: A namedtuple
        """

        _columns, _values = ParseParameters.parse_insert_params(params)

        sql = f"""
        INSERT INTO {table} ({_columns}) VALUES ({_values})
        """

        print()
        print(sql)

        try:
            # Execute sql
            self.logger.info(f"Inserting record in {table}")
            cursor = self.execute_sql(sql)

            # Get the number of rows
            self.logger.info(f"{cursor.rowcount} rows")
            print(f"Inserted {cursor.rowcount}row(s) into {table}")

            # Close communication with the PostgreSQL database
            cursor.close()

        except (Exception, psycopg2.DatabaseError) as error:
            raise

    def read(self, table, columns, filters):
        """
        Fetch records
        """
        _columns = ", ".join(columns)
        _filters = ParseParameters.parse_filters(filters)

        sql = f"SELECT {_columns} FROM {table} {_filters};"
        try:
            # Execute sql
            self.logger.info(f"Reading from {table} table")
            cursor = self.execute_sql(sql)

            # Get the number of rows
            self.logger.info(f"Returned {cursor.rowcount}row(s)")

            shoppers = []
            for row in cursor.fetchall():
                uid, username, email = row
                shopper = {
                    "uid": uid,
                    "username": username,
                    "email": email,
                }
                shoppers.append(shopper)

            # Close communication with the PostgreSQL database
            cursor.close()

            return shoppers

        except (Exception, psycopg2.DatabaseError) as error:
            raise

    def update(self, table, params, filters):
        """
        Edit record
        """

        _update_cols = ParseParameters.parse_update_params(params)
        _filters = ParseParameters.parse_filters(filters)

        sql = f"UPDATE {table} SET {_update_cols} {_filters}"
        try:
            # Execute sql
            self.logger.info(f"Updating records in {table}")
            cursor = self.execute_sql(sql)

            # Get the number of rows updates
            self.logger.info(f"{cursor.rowcount} rows")
            print(f"Updated {cursor.rowcount}row(s) in {table}")

            # Close communication with the PostgreSQL database
            cursor.close()

        except (Exception, psycopg2.DatabaseError) as error:
            raise

    def delete(self, table, filters):
        """
        Delete record
        """
        _filters = ParseParameters.parse_filters(filters)

        sql = f"DELETE FROM {table} {_filters};"
        try:
            # Execute sql
            self.logger.info(f"Deleting from {table} table")
            cursor = self.execute_sql(sql)

            # Get the number of rows
            self.logger.info(f"Deleted {cursor.rowcount}row(s)")

            # Close communication with the PostgreSQL database
            cursor.close()

        except (Exception, psycopg2.DatabaseError) as error:
            raise
