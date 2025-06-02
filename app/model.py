# app/model.py
from app.preprocess import extract_keywords
from app.database import get_db_connection

def generate_sql_query(text):
    keywords = extract_keywords(text)
    # Example logic (replace with your actual SQL generation)
    return f"SELECT * FROM table WHERE column IN {tuple(keywords)}"

def execute_query(query):
    conn = get_db_connection()
    result = conn.execute(query).fetchall()
    conn.close()
    return result