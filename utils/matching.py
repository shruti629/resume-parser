from rapidfuzz import fuzz
from collections import Counter
import re

def calculate_match_score(resume_text, jd_text):
    return fuzz.token_sort_ratio(resume_text, jd_text)


def find_missing_keywords(resume_text, jd_text, top_n=10):
    # Predefined skills dictionary (expand as needed)
    skills_db = {
        "python", "java", "c++", "sql", "mysql", "postgresql", "mongodb",
        "machine learning", "deep learning", "data analysis", "nlp", "pandas",
        "numpy", "excel", "tableau", "power bi", "aws", "azure", "gcp", 
        "docker", "kubernetes", "git", "flask", "django", "html", "css", "javascript",
        "leadership", "communication", "teamwork", "problem solving",
        "time management", "project management", "design thinking", 
        "finance", "marketing", "business analysis", "cloud computing"
    }

    # Extract words from JD and resume
    jd_words = re.findall(r'\b\w+\b', jd_text.lower())
    resume_words = set(re.findall(r'\b\w+\b', resume_text.lower()))

    # Frequency count in JD
    word_freq = Counter(jd_words)

    # Keep only keywords that exist in skills_db
    jd_keywords = {word for word in jd_words if word in skills_db}

    # Missing skills
    missing_keywords = jd_keywords - resume_words

    # Sort by frequency in JD
    important_missing = sorted(missing_keywords, key=lambda w: word_freq[w], reverse=True)

    # Return top N
    return important_missing[:top_n]