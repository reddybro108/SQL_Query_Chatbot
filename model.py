import sqlite3
from preprocess import extract_keywords

def generate_sql_query(user_input):
    keywords = extract_keywords(user_input)
    select_clause = "SELECT * FROM employees"
    where_clause = ""
    order_by_clause = ""

    # Simple rule-based parsing
    if "salary" in keywords and any(word in keywords for word in ["above", "greater", "more"]):
        for i, word in enumerate(keywords):
            if word in ["above", "greater", "more"] and i + 1 < len(keywords) and keywords[i + 1].isdigit():
                where_clause = f"WHERE salary > {keywords[i + 1]}"
                break
    elif "department" in keywords:
        for i, word in enumerate(keywords):
            if word == "department" and i + 1 < len(keywords):
                where_clause = f"WHERE department = '{keywords[i + 1].capitalize()}'"
                break
    if "sort" in keywords or "order" in keywords:
        if "salary" in keywords:
            order_by_clause = "ORDER BY salary DESC"

    query = f"{select_clause} {where_clause} {order_by_clause}".strip()
    return query

def execute_query(query):
    conn = sqlite3.connect('employees.db')
    cursor = conn.cursor()
    try:
        cursor.execute(query)
        columns = [desc[0] for desc in cursor.description]
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]
    except sqlite3.Error as e:
        results = {"error": str(e)}
    finally:
        conn.close()
    return results