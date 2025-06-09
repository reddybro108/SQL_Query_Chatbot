from fastapi import FastAPI
from pydantic import BaseModel
import pymysql
from app.database import get_connection  # Assuming this is where process_query or similar is defined

app = FastAPI()


class QueryRequest(BaseModel):
    text: str


def generate_sql_query(user_input: str) -> str:
    # Replace with your query processing logic
    # For now, return a placeholder SQL query or handle invalid input
    if "invalid" in user_input.lower():
        raise ValueError("Invalid query provided")
    # Example: Convert natural language to SQL (simplified)
    if "research department" in user_input.lower():
        return "SELECT * FROM users WHERE department = 'research'"
    return user_input  # Placeholder; replace with actual logic


@app.get("/")
async def root():
    return {"message": "Welcome to the SQL Query Chatbot API"}


@app.post("/query/")
async def run_query(request: QueryRequest):
    try:
        sql_query = generate_sql_query(request.query)  # Use request.query, not request.text
        conn = get_connection()
        try:
            with conn.cursor() as cursor:
                cursor.execute(sql_query)
                result = cursor.fetchall()
            return {"result": result}
        finally:
            conn.close()
    except Exception as e:
        return {"error": f"Query failed: {str(e)}"}
