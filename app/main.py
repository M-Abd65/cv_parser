# main.py
from fastapi import FastAPI, UploadFile, File
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base, CVInfo, Skill, Language, Experience, Education
from app.parser import parse_cv_with_gpt
from dotenv import load_dotenv

import json
import os
import tempfile
from pdfminer.high_level import extract_text
from datetime import datetime

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

# Create tables
Base.metadata.create_all(engine)

app = FastAPI()

def parse_date(date_str):
    """Convert date string to date object, return None if invalid or empty."""
    if not date_str or not isinstance(date_str, str):
        return None
    for fmt in ("%Y-%m-%d", "%d/%m/%Y", "%m/%Y", "%Y"):
        try:
            return datetime.strptime(date_str, fmt).date()
        except ValueError:
            continue
    return None  # Could log warning here if needed

@app.post("/parse-cv/")
async def parse_cv(file: UploadFile = File(...)):
    if file.content_type != "application/pdf":
        return {"error": "Only PDF files are supported."}

    # Save the uploaded PDF temporarily
    file_content = await file.read()  # Read file content here
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(file_content)
        tmp_path = tmp.name

    try:
        cv_text = extract_text(tmp_path)
    finally:
        os.remove(tmp_path)
    # Use your GPT-based parser
    parsed_data = parse_cv_with_gpt(cv_text)
    parsed_json = json.loads(parsed_data)

    db = SessionLocal()

    # Save into DB
    cv_info = CVInfo(
        firstname=parsed_json["info"]["firstname"],
        lastname=parsed_json["info"]["lastname"],
        gender=parsed_json["info"]["gender"] or None,
        datebirth=parse_date(parsed_json["info"]["datebirth"]),
        cv_content=file_content
    )
    db.add(cv_info)
    db.commit()
    db.refresh(cv_info)

    for skill in parsed_json["skills"]:
        db.add(Skill(name=skill["name"], level=skill["level"], cv_id=cv_info.id))

    for lang in parsed_json["languages"]:
        db.add(Language(name=lang["name"], level=lang["level"], cv_id=cv_info.id))

    for exp in parsed_json["experiences"]:
        db.add(Experience(
            title=exp["title"],
            description=exp["description"],
            company=exp["company"],
            date_start=parse_date(exp["date_start"]),
            date_end=parse_date(exp["date_end"]),
            cv_id=cv_info.id
        ))

    for edu in parsed_json["educations"]:
        db.add(Education(
            degree=edu["degree"],
            institution=edu["institution"],
            date_start=parse_date(edu["date_start"]),
            date_end=parse_date(edu["date_end"]),
            cv_id=cv_info.id
        ))

    db.commit()

    return parsed_json