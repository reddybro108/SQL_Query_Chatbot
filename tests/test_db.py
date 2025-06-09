# tests/test_db.py
from app.database import get_connection


def test_db_connection():
    """Test connection to the database."""
    try:
        conn = get_connection()
        with conn.cursor() as cursor:
            cursor.execute("SELECT 1")
            result = cursor.fetchone()
        assert result == {"1": 1}
    finally:
        conn.close()
