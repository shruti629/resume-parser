import streamlit as st
from utils.extract_text import extract_resume_text
from utils.matching import calculate_match_score, find_missing_keywords
from utils.nlp_processing import extract_entities
from utils.suggestions import get_resume_improvement
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import io
import json
import tempfile

st.set_page_config(page_title="Resume Parser", page_icon="📄", layout="wide")

st.title("📄 AI Resume Parser")
st.markdown("Upload your resume, and optionally paste the job description for AI-powered matching.")

uploaded_file = st.file_uploader("📤 Upload Resume (PDF/DOCX)", type=["pdf", "docx"])
job_description = st.text_area("📝 Paste Job Description (optional)", height=150)

# Add button to submit
if st.button("Analyze"):
    if uploaded_file:
        resume_text = extract_resume_text(uploaded_file)

        if resume_text:
            # Extracted info
            entities = extract_entities(resume_text)

            st.subheader(" Extracted Information")
            st.write(entities)

            # Always allow JSON download for extracted info
            json_data = {
                "job_description": job_description if job_description else None,
                "extracted_information": entities
            }

            # If JD is given, add more analysis
            if job_description.strip():
                match_score = calculate_match_score(resume_text, job_description)
                missing_keywords = find_missing_keywords(resume_text, job_description)
                suggestions = get_resume_improvement(resume_text, job_description)

                json_data.update({
                    "match_score": match_score,
                    "missing_keywords": missing_keywords,
                    "suggestions": suggestions
                })

                # Missing keywords in text format
                #st.subheader("📌 Missing Keywords")
                #st.write(", ".join(missing_keywords) if missing_keywords else "None")

                # AI suggestions
                st.subheader("💡 AI Suggestions")
                st.markdown(suggestions)

                # PDF download
                buffer = io.BytesIO()
                c = canvas.Canvas(buffer, pagesize=letter)
                c.drawString(50, 750, "AI Resume Analysis Report")
                c.drawString(50, 730, f"Match Score: {match_score}%")
                c.drawString(50, 710, f"Missing Keywords: {', '.join(missing_keywords)}")
                c.drawString(50, 690, "Suggestions:")
                text_object = c.beginText(50, 670)
                for line in suggestions.split("\n"):
                    text_object.textLine(line)
                c.drawText(text_object)
                c.save()
                buffer.seek(0)

                st.download_button(
                    label="📥 Download AI Report (PDF)",
                    data=buffer,
                    file_name="resume_report.pdf",
                    mime="application/pdf"
                )

            # JSON download (works both with/without JD)
            json_file_path = tempfile.NamedTemporaryFile(delete=False, suffix=".json").name
            with open(json_file_path, "w") as json_file:
                json.dump(json_data, json_file, indent=4)

            with open(json_file_path, "rb") as f:
                st.download_button(
                    label="📥 Download Extracted Data (JSON)",
                    data=f,
                    file_name="resume_data.json",
                    mime="application/json"
                )

        else:
            st.error(" Unsupported file format. Please upload PDF or DOCX.")
    else:
        st.error("Please upload your resume first.")


