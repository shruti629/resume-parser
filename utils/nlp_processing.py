import spacy
import re

nlp = spacy.load("en_core_web_sm")

def extract_entities(text):
    doc = nlp(text)
    entities = {
        "name": None,
        "email": None,
        "phone": None,
        "skills": [],
        "education": [],
        "experience": []
    }


    #  Extract Name (hybrid approach)
    # Try first 3 lines of resume
    first_lines = text.strip().split("\n")[:3]
    for line in first_lines:
        line = line.strip()
        if len(line.split()) <= 4 and not re.search(r"[@\d]", line):  # no numbers/emails
            entities["name"] = line
            break

    # If still not found, fallback to PERSON entity from spaCy
    if not entities["name"]:
        for ent in doc.ents:
            if ent.label_ == "PERSON":
                entities["name"] = ent.text
                break

    # Email
    match_email = re.search(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", text)
    if match_email:
        entities["email"] = match_email.group()

    # Phone
    match_phone = re.search(r"\+?\d[\d\s\-]{8,}\d", text)
    if match_phone:
        entities["phone"] = match_phone.group()

    # Education & Experience
    # Section-based splitting
    sections = re.split(r"(?i)(education|experience|work experience|skills|certifications)", text)
    
    for i, sec in enumerate(sections):
        sec_lower = sec.lower()
        if "education" in sec_lower:
            entities["education"].append(sections[i+1].strip())
        elif "experience" in sec_lower or "work experience" in sec_lower:
            entities["experience"].append(sections[i+1].strip())

    # Simple skill extraction (keywords)
    common_skills = ["python", "java", "sql", "excel", "machine learning", "deep learning", "data analysis", "c++", "html", "css", "javascript"]
    for skill in common_skills:
        if skill.lower() in text.lower():
            entities["skills"].append(skill)

    return entities


