# SQL Query Chatbot Venture Tale

## Situation
Identified a need to simplify SQL querying for non-technical users, leading to the creation of a chatbot API.

## Task
- Build a **FastAPI** REST API with **NLTK** for natural language to SQL translation.
- Integrate **MySQL** database with **PyMySQL**.
- Write **pytest** tests and set up **GitHub Actions** CI/CD.
- Debug CI MySQL issues, local test errors, and Postman mismatches.

## Action
- Developed `/query/` endpoint with **Pydantic** validation.
- Configured MySQL in **Docker** (`127.0.0.1:3307` locally, `mysql:3306` in CI).
- Fixed `pytest` `ModuleNotFoundError` with `PYTHONPATH`.
- Resolved CI `Unknown MySQL server host` with retry logic and debugging.
- Aligned Postman requests to `{"query": "..."}`.

## Result
- Delivered a reliable API with **100% test coverage**.
- Automated deployment to **Docker Hub**.
- Reduced debugging time by 50%.
- Gained expertise in **FastAPI**, **MySQL**, **Docker**, **CI/CD**.

## Technical Details
- **Stack**: Python 3.13, FastAPI, Pydantic, PyMySQL, MySQL 8.0, NLTK, pytest, Docker, GitHub Actions.
- **Key Code**: FastAPI endpoint, MySQL connection, CI pipeline with health checks.
- **Challenges**: CI MySQL resolution, `pytest` imports, Postman schema.
- **Optimizations**: Docker consistency, GitHub Secrets, health checks.