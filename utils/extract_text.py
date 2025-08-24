import pdfplumber
import docx
import re
from collections import Counter

# --- Resume Extraction ---
def extract_text_from_pdf(pdf_file):
    text = ""
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text.strip()

def extract_text_from_docx(docx_file):
    doc = docx.Document(docx_file)
    text = "\n".join([para.text for para in doc.paragraphs if para.text.strip()])
    return text.strip()

def extract_resume_text(file):
    if file.name.endswith(".pdf"):
        return extract_text_from_pdf(file)
    elif file.name.endswith(".docx"):
        return extract_text_from_docx(file)
    else:
        return None

# --- Missing Keywords Detection ---
def get_main_missing_keywords(resume_text, job_description, top_n=10):
    # Convert to lowercase and extract words
    jd_words = re.findall(r'\b[a-zA-Z]+\b', job_description.lower())
    resume_words = set(re.findall(r'\b[a-zA-Z]+\b', resume_text.lower()))

    # Common stopwords to ignore
    stopwords = set([
        "and", "or", "the", "is", "in", "to", "a", "of", "for", "on", "with", 
        "by", "an", "at", "as", "are", "from", "be", "this", "that", "will",
    ])
    jd_keywords = [word for word in jd_words if word not in stopwords]

    # Count frequency of each keyword in JD
    keyword_freq = Counter(jd_keywords)

    # Find missing keywords sorted by importance (frequency)
    missing_keywords = [word for word, _ in keyword_freq.most_common()
                        if word not in resume_words]

    return missing_keywords[:top_n]


