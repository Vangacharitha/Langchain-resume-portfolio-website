import streamlit as st
import os
import zipfile
from dotenv import load_dotenv

from pypdf import PdfReader
import docx

from langchain_google_genai import ChatGoogleGenerativeAI


load_dotenv()
os.environ["GOOGLE_API_KEY"] = os.getenv("gemini")


LINKEDIN_URL = "https://www.linkedin.com/in/charitha-vanga/"
GITHUB_URL = "https://github.com/Vangacharitha"


st.set_page_config(
    page_title="AI Resume Portfolio Generator",
    page_icon="✨",
    layout="centered"
)

st.title(":rainbow[AI Resume → Interactive Portfolio Generator]")
st.write("Upload your resume and get a premium, recruiter-ready portfolio website 🚀")



uploaded_resume = st.file_uploader(
    "📄 Upload Resume (PDF or DOCX)",
    type=["pdf", "docx"]
)


def extract_resume_text(uploaded_file):
    text = ""

    if uploaded_file.type == "application/pdf":
        reader = PdfReader(uploaded_file)
        for page in reader.pages:
            text += page.extract_text() or ""

    elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        doc = docx.Document(uploaded_file)
        for para in doc.paragraphs:
            text += para.text + "\n"

    return text


if st.button("🚀 Generate Portfolio Website"):

    if uploaded_resume is None:
        st.error("Please upload your resume first")
        st.stop()

    resume_text = extract_resume_text(uploaded_resume)

    
    system_prompt = """
You are a SENIOR UI/UX DESIGNER and FRONTEND ENGINEER.

Create a PREMIUM, MODERN, and INTERACTIVE personal portfolio website.

DESIGN QUALITY:
- High-end, professional, recruiter-ready
- Smooth animations
- Clean typography
- Responsive design

SECTIONS:
1. Hero (Name, Role, CTA buttons)
2. About Me
3. Skills
4. Projects
5. Contact

SKILLS RULES (VERY IMPORTANT):
- DO NOT show percentages
- DO NOT use progress bars
- Show skills as clean tags or cards ONLY

PROJECT RULES:
- Project cards must be clickable
- Clicking opens GitHub or LinkedIn project link
- Use hover animations

CONTACT SECTION RULES:
- MUST include LinkedIn and GitHub
- Use EXACT URLs provided
- Entire text/icon must be clickable
- Use <a href="URL" target="_blank" rel="noopener noreferrer">
- NEVER use # or empty href

TECH RULES:
- HTML, CSS, JavaScript ONLY
- No React, no Bootstrap, no Tailwind
- Clean and semantic code

STRICT OUTPUT FORMAT (NO EXTRA TEXT):

--html--
[HTML CODE]
--html--

--css--
[CSS CODE]
--css--

--js--
[JAVASCRIPT CODE]
--js--
"""

    
    messages = [
        ("system", system_prompt),
        ("user", f"""
Resume Content:
{resume_text}

MANDATORY SOCIAL LINKS (USE EXACTLY):
LinkedIn: {LINKEDIN_URL}
GitHub: {GITHUB_URL}

Additional Instructions:
None
""")
    ]

    model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")
    response = model.invoke(messages)

    content = response.content

    # ---------------- SPLIT OUTPUT ----------------
    try:
        html_code = content.split("--html--")[1].split("--html--")[0]
        css_code = content.split("--css--")[1].split("--css--")[0]
        js_code = content.split("--js--")[1].split("--js--")[0]
    except Exception:
        st.error("AI output format error. Please try again.")
        st.stop()

    
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html_code)

    with open("style.css", "w", encoding="utf-8") as f:
        f.write(css_code)

    with open("script.js", "w", encoding="utf-8") as f:
        f.write(js_code)

    
    with zipfile.ZipFile("portfolio_website.zip", "w") as zipf:
        zipf.write("index.html")
        zipf.write("style.css")
        zipf.write("script.js")

    
    st.success("✅ Premium Portfolio Website Generated Successfully!")
    st.download_button(
        label="📥 Download Portfolio Website (ZIP)",
        data=open("portfolio_website.zip", "rb"),
        file_name="portfolio_website.zip",
        mime="application/zip"
    )
