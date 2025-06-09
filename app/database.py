import pymysql
from pymysql.cursors import DictCursor

# Database configuration (replace with your actual credentials)
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "Amolreddy@108",
    "database": "amoldb",
    "charset": "utf8mb4",
    "cursorclass": DictCursor  # Returns query results as dictionaries
}


def get_db_connection():
    try:
        connection = pymysql.connect(**DB_CONFIG)
        return connection
    except pymysql.MySQLError as e:
        raise Exception(f"Database connection failed: {str(e)}")
