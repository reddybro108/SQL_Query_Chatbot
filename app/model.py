import os
import nltk
import pymysql

from app.preprocess import extract_keywords
from app.database import get_db_connection


nltk_data_path = os.path.join(os.path.dirname(__file__), 'nltk_data')
nltk.data.path.append(nltk_data_path)


def download_nltk_data():
    try:
        nltk.data.find('tokenizers/punkt')
    except LookupError:
        nltk.download('punkt', download_dir=nltk_data_path)
    try:
        nltk.data.find('corpora/stopwords')
    except LookupError:
        nltk.download('stopwords', download_dir=nltk_data_path)


def generate_sql_query(text):
    text = text.lower()
    keywords = extract_keywords(text)

    if "employees" in keywords:
        query = "SELECT * FROM employees"
        conditions = []

        if "research" in keywords:
            conditions.append("department = 'Research'")
        if "top" in keywords and "salary" in keywords:
            order_by = " ORDER BY salary DESC LIMIT 10"
        else:
            order_by = ""

        if conditions:
            query += " WHERE " + " AND ".join(conditions)
        query += order_by

        return query

    return "SELECT * FROM users"  # fallback


def execute_query(query):
    conn = get_db_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchone()
        conn.commit()
        return result
    except pymysql.MySQLError as e:
        raise Exception(f"Query execution failed: {str(e)}")
    finally:
        conn.close()
