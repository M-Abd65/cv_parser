# parser.py
from langchain_community.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import os
load_dotenv()


OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def parse_cv_with_gpt(cv_text: str):
    llm = ChatOpenAI(model_name="gpt-4", temperature=0, openai_api_key=OPENAI_API_KEY)

    prompt = PromptTemplate(
        input_variables=["cv"],
        template="""
Extract the following information from the CV text:

Return it strictly in this JSON format:

{{
  "info": {{
    "firstname": "", "lastname": "", "gender": "", "datebirth": ""
  }},
  "skills": [
    {{"name": "", "level": ""}}
  ],
  "languages": [
    {{"name": "", "level": ""}}
  ],
  "experiences": [
    {{"title": "","company":"", "description": "", "date_start": "", "date_end": ""}}
  ],
  "educations": [
    {{"degree": "", "institution": "", "date_start": "", "date_end": ""}}
  ]
}}

CV:
{cv}
        """
    )

    full_prompt = prompt.format(cv=cv_text)
    response = llm.predict(full_prompt)
    return response
