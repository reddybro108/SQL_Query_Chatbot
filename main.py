from fastapi import FastAPI
from pydantic import BaseModel
from model import generate_sql_query, execute_query

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the SQL Query Chatbot API"}

class Query(BaseModel):
    user_input: str

@app.post("/query/")
def process_query(query: Query):
    sql_query = generate_sql_query(query.user_input)
    results = execute_query(sql_query)
    return {"sql_query": sql_query, "results": results}
