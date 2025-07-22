import streamlit as st
from utils.parser import extract_text
from utils.analyzer import analyze_resume

def home_page():
    st.title("📄 Resume Analyzer Dashboard")
    st.write("Upload your resume and paste job description:")

    resume_file = st.file_uploader("Upload Resume (PDF/DOCX)", type=["pdf", "docx"])
    job_desc = st.text_area("Paste Job Description", height=200)

    if st.button("Analyze"):
        if resume_file and job_desc:
            try:
                resume_text = extract_text(resume_file)
                score, feedback = analyze_resume(resume_text, job_desc)
                st.success(f"Match Score: {score:.2f}%")
                st.markdown("### Feedback")
                st.info(feedback)
            except Exception as e:
                st.error(f"Error: {str(e)}")
        else:
            st.error("Upload resume and paste job description.")

    if st.button("Logout"):
        st.session_state.pop("user", None)
        st.experimental_rerun()
