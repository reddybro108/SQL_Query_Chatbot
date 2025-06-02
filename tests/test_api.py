# app/main.py
from fastapi import FastAPI
from app.model import generate_sql_query, execute_query

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello, World!"}


@app.post("/query/")
async def query(text: str):
    sql_query = generate_sql_query(text)
    result = execute_query(sql_query)
    return {"query": sql_query, "result": result}
