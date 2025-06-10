from fastapi import FastAPI
from pydantic import BaseModel
from app.database import get_connection

app = FastAPI()


class QueryRequest(BaseModel):
    query: str


def generate_sql_query(user_input: str) -> str:
    # Placeholder; replace with your query processing logic
    if "invalid" in user_input.lower():
        raise ValueError("Invalid query provided")
    if "research department" in user_input.lower():
        return "SELECT * FROM users WHERE department = 'research'"
    return user_input


@app.get("/")
async def root():
    return {"message": "Welcome to the SQL Query Chatbot API"}


@app.post("/query/")
async def run_query(request: QueryRequest):
    try:
        sql_query = generate_sql_query(request.query)  # Use request.query
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
