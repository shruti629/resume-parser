import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def get_resume_improvement(resume_text, jd_text):
    prompt = f"""
    You are an expert resume consultant.
    Resume: {resume_text}
    Job Description: {jd_text}
    Task:
    1. Give few improvement suggestions to make this resume more ATS-friendly.
    2. Suggest few additional skills or keywords to add based on job description.
    Output in bullet points.
    """
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    return response.text
