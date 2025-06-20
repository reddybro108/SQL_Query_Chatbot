import os
import pymysql
from pymysql.cursors import DictCursor


def init_db():
    config = {
        "host": os.getenv("DB_HOST", "127.0.0.1"),
        "port": int(os.getenv("DB_PORT", 3307)),
        "user": os.getenv("DB_USER", "root"),
        "password": os.getenv("DB_PASSWORD", "Amolreddy@108"),
        "database": os.getenv("DB_NAME", "amoldb"),
        "charset": "utf8mb4",
        "cursorclass": DictCursor,
    }
    conn = pymysql.connect(**config)
    try:
        with conn.cursor() as cursor:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(255),
                    age INT,
                    department VARCHAR(255)
                )
            """)
            cursor.execute("""
                INSERT IGNORE INTO users (name, age, department) VALUES
                ('Alice', 30, 'research'),
                ('Bob', 25, 'engineering')
            """)
            conn.commit()
    finally:
        conn.close()


if __name__ == "__main__":
    init_db()
