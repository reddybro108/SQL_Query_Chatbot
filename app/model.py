import pymysql

from app.database import get_connection
from app.preprocess import extract_keywords


def sanitize_input(text: str) -> str:
    """
    Remove potentially harmful SQL keywords to prevent injection.

    Args:
        text: Input query string.

    Returns:
        Sanitized query string.

    Raises:
        ValueError: If restricted keywords are found.
    """
    dangerous_keywords = ["DROP", "DELETE", "TRUNCATE", "ALTER", "INSERT", "UPDATE"]
    text_upper = text.upper()
    for keyword in dangerous_keywords:
        if keyword in text_upper:
            raise ValueError(f"Invalid query: contains restricted keyword '{keyword}'")
    return text.lower()


def generate_sql_query(text: str) -> str:
    """
    Generate SQL query from natural language input.

    Args:
        text: Natural language query.

    Returns:
        SQL query string.
    """
    text = sanitize_input(text)
    keywords = extract_keywords(text)
    if "users" in keywords and "age" in keywords:
        return "SELECT * FROM users WHERE age > 30"
    elif "products" in keywords and "price" in keywords:
        return "SELECT * FROM products WHERE price < 100"
    elif "orders" in keywords:
        return "SELECT * FROM orders"
    return "SELECT * FROM users"


def execute_query(query: str) -> list:
    """
    Execute SQL query and return results.

    Args:
        query: SQL query string.

    Returns:
        List of query results.

    Raises:
        Exception: If query execution fails.
    """
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
        conn.commit()
        return result
    except pymysql.MySQLError as e:
        raise Exception(f"Query execution failed: {str(e)}")
    finally:
        conn.close()
