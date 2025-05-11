# CV Parser App

A project using FastAPI, LangChain, and Streamlit to parse and display CV information.

## Features
1. FastAPI for parsing and storing CV data
2. PostgreSQL + SQLAlchemy for persistence
3. Streamlit UI for easy interaction

## Setup

### Without Docker

1. Clone the repo
2. Create a virtual environment
3. Install requirements:
   ```bash
   pip install -r requirements.txt

4. Run the backend:
uvicorn app.main:app --reload

5. Run the frontend:
streamlit run streamlit_app/app.py

### With Docker (Recommended for Easy Deployment)
1. Clone the repo

2. Make sure you have Docker installed on your machine. If not, you can install it from here.

3. Navigate to the project folder containing the docker-compose.yml file.

4. Build the Docker containers:
docker-compose up --build

5. The app will be available at the following URLs:
* FastAPI backend: http://localhost:8000

* Streamlit frontend: http://localhost:8501

### Docker Notes:
* The Docker setup includes both the FastAPI backend and PostgreSQL, so no need to set up a local database.

* The database and application containers will automatically be created when you run docker-compose up