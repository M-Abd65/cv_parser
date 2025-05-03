# CV Parser App

A project using FastAPI, langachain and Streamlit to parse and display CV information.

## Features
1. FastAPI for parsing and storing CV data

2. PostgreSQL + SQLAlchemy for persistence

3. Streamlit UI for easy interaction

## Setup

1. Clone the repo
2. Create a virtual environment
3. Install requirements:
   ```bash
   pip install -r requirements.txt
4. run the backend:
    uvicorn app.main:app --reload
5. run the frontend:
    streamlit run streamlit_app/app.py

