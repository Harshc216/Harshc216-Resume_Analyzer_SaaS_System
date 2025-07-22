import streamlit as st
from database import init_db
from auth import login_page
from home import home_page

st.set_page_config(page_title="Resume Analyzer", layout="centered")
init_db()

if "user" not in st.session_state:
    login_page()
else:
    home_page()
