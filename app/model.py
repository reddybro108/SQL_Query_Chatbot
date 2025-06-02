# app/model.py
from app.preprocess import extract_keywords
from app.database import get_db_connection

def generate_sql_query(text):
    keywords = extract_keywords(text)
    return f"SELECT * FROM table WHERE column IN {tuple(keywords)}"

def execute_query(query):
    conn = get_db_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
        conn.commit()
        return result
    finally:
        conn.close()