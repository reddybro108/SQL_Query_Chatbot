# app/database.py
import os

import pymysql
from pymysql.cursors import DictCursor


def get_connection() -> pymysql.connections.Connection:
    """Establish a connection to the MySQL database.

    Returns:
        pymysql.connections.Connection: Active database connection.

    Raises:
        Exception: If connection fails due to MySQL error.
    """
    config = {
        "host": os.getenv("DB_HOST", "127.0.0.1"),
        "port": int(os.getenv("DB_PORT", 3307)),
        "user": os.getenv("DB_USER", "root"),
        "password": os.getenv("DB_PASSWORD", "Amolreddy@108"),
        "database": os.getenv("DB_NAME", "amoldb"),
        "charset": "utf8mb4",
        "cursorclass": DictCursor,
    }
    try:
        return pymysql.connect(**config)
    except pymysql.MySQLError as e:
        raise Exception(f"Database connection failed: {str(e)}")
