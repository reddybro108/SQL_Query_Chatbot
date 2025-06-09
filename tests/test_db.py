from app.database import get_connection


def test_db_connection():
    """Test connection to the database."""
    conn = None
    try:
        conn = get_connection()
        with conn.cursor() as cursor:
            cursor.execute("SELECT 1")
            result = cursor.fetchone()
        assert result == {"1": 1} or result == (1,)  # depends on fetch style
    finally:
        if conn:
            conn.close()
