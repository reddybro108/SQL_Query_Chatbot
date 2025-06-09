from fastapi import FastAPI
from pydantic import BaseModel
from app.model import generate_sql_query, execute_query

app = FastAPI()


class QueryRequest(BaseModel):
    text: str


@app.get("/")
def root():
    return {"message": "Welcome to the SQL Query Chatbot!"}


@app.post("/query/")
def run_query(request: QueryRequest):
    sql = generate_sql_query(request.text)
    result = execute_query(sql)
    return {
        "query": sql,
        "result": result
    }
