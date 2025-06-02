# SQL Query Chatbot

A FastAPI-based chatbot that converts natural language queries into SQL queries, executes them on a SQLite database, and returns results. The project is containerized with Docker and includes a GitHub Actions CI/CD pipeline.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Testing](#testing)
- [Docker Setup](#docker-setup)
- [CI/CD Pipeline](#cicd-pipeline)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Overview
`SQL_Query_Chatbot` is a Python-based chatbot that translates natural language inputs into SQL queries using rule-based parsing and NLTK for text preprocessing. It operates on a SQLite database (`employees.db`) and is deployed as a Docker container.

## Features
- Converts natural language to SQL queries.
- Executes queries on a SQLite database.
- FastAPI backend for high-performance API.
- NLTK-based text preprocessing.
- Dockerized deployment.
- Automated CI/CD with GitHub Actions.
- Unit tests with pytest.

## Prerequisites
- Python 3.13
- Docker
- Git
- Postman (optional)
- GitHub and Docker Hub accounts

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/reddybro108/SQL_Query_Chatbot.git
   cd SQL_Query_Chatbot
   ```
2. Set up virtual environment:
   ```bash
   python -m venv sqlenv
   .\sqlenv\Scripts\Activate.ps1  # Windows
   source sqlenv/bin/activate  # Linux/macOS
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Download NLTK data:
   ```bash
   python -c "import nltk; nltk.download('punkt', download_dir='nltk_data'); nltk.download('stopwords', download_dir='nltk_data')"
   ```
5. Initialize database:
   ```bash
   python init_db.py
   ```

## Usage
1. Run the FastAPI application:
   ```bash
   uvicorn main:app --reload
   ```
2. Test with Postman:
   - **Method**: POST
   - **URL**: `http://127.0.0.1:8000/query/`
   - **Body**:
     ```json
     {
       "user_input": "Show employees with salary above 60000"
     }
     ```
   - **Response**:
     ```json
     {
       "sql_query": "SELECT * FROM employees WHERE salary > 60000",
       "results": [{"id": 2, "name": "Bob", "department": "IT", "salary": 75000}, ...]
     }
     ```

## API Endpoints
- **POST `/query/`**
  - **Description**: Converts natural language to SQL and returns results.
  - **Request Body**:
    ```json
    {
      "user_input": "string"
    }
    ```
  - **Response**:
    ```json
    {
      "sql_query": "string",
      "results": [{}]
    }
    ```

## Testing
Run tests:
```bash
python -m pytest tests
```

## Docker Setup
1. Build the image:
   ```bash
   docker build -t reddybro108/sql-query-chatbot:latest .
   ```
2. Run the container:
   ```bash
   docker run -d -p 8000:8000 --name sql-query-chatbot reddybro108/sql-query-chatbot:latest
   ```

## CI/CD Pipeline
Defined in `.github/workflows/main.yml`:
- **Build Job**: Runs tests and syntax checks.
- **Dockerize Job**: Builds and pushes the Docker image.

Set up secrets in GitHub:
- `DOCKER_USERNAME`
- `DOCKER_PASSWORD`

## Project Structure
```
SQL_Query_Chatbot/
├── .github/workflows/main.yml
├── tests/test_api.py
├── nltk_data/
├── .dockerignore
├── Dockerfile
├── main.py
├── model.py
├── preprocess.py
├── init_db.py
├── requirements.txt
├── employees.db
└── README.md
```

## Contributing
1. Fork the repository.
2. Create a feature branch.
3. Commit changes.
4. Push and open a pull request.

## License
MIT License. See [LICENSE](LICENSE).