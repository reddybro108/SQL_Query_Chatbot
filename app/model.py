import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from app.preprocess import extract_keywords, download_nltk_data
from app.database import get_db_connection
import pymysql

def extract_keywords(text):
    return [word.lower() for word in text.split() if len(word) > 3]

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


if __name__ == "__main__":
    download_nltk_data()
    test_query = "SELECT * FROM employees"
    try:
        result = execute_query(test_query)
        print(result)
    except Exception as e:
        print(f"Error: {e}")

query='SELECT * FROM employees'
print(execute_query(query))
