# test_db.py
from app.database import get_db_connection
try:
    conn = get_db_connection()
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM users")
        print(cursor.fetchall())
    conn.close()
except Exception as e:
    print(f"Error: {e}")
