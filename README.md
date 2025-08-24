# 📄 AI-Powered Resume Parser

An AI-powered Resume Parsing and Analysis tool built with **Streamlit, spaCy, and NLP**.  
This tool extracts key information from resumes (PDF/DOCX), analyzes them against a given job description, and provides **ATS-friendly improvement suggestions**.



## 🚀 Features
- Upload **resume files (PDF/DOCX)**
- Extract key details:
  - Name  
  - Email  
  - Phone  
  - Skills  
  - Experience  
  - Education  
- Optionally paste a **Job Description (JD)**
- Get **AI-powered suggestions**:
  1. Improve resume formatting for ATS
  2. Add missing **skills/keywords** based on the JD
- Download:
  - Extracted resume data in **JSON**
  - AI suggestions in **text**



## 🛠️ Tech Stack
- [Python](https://www.python.org/)  
- [Streamlit](https://streamlit.io/)  
- [spaCy](https://spacy.io/) (`en_core_web_sm` model)  
- [PyPDF2](https://pypi.org/project/PyPDF2/)  
- [docx2txt](https://pypi.org/project/docx2txt/)  
- OpenAI / HuggingFace (for AI suggestions)




## ⚡ Installation & Setup

1. Clone the repository:
   ```bash
       git clone https://github.com/your-username/resume-parser.git
       cd resume-parser
2. Create and activate a virtual environment:
   
       python -m venv venv
       source venv/bin/activate   # Mac/Linux
       venv\Scripts\activate      # Windows  
3. Install dependencies:
   ```bash
    pip install -r requirements.txt 
4. **Google Gemini API**
   
   Get your API key from https://aistudio.google.com

   Set it as an environment variable:

       export GEMINI_API_KEY="your_gemini_api_key"   # Mac/Linux
       setx GEMINI_API_KEY "your_gemini_api_key"     # Windows 
5. Run the app:
   ```bash
   streamlit run app.py
   
## 🎯 Usage

1.) Upload your **Resume (PDF/DOCX)**

2.) (Optional) Paste the **Job Description**

3.) Click **Analyze**

4.) View:

5.) Extracted resume data

6.) ATS improvement suggestions

Download results as **JSON or TXT**

## License

This project is licensed under the MIT License.







