import streamlit as st
from database import register_user, login_user

def login_page():
    st.title("🔐 Login or Sign Up")
    action = st.radio("Choose Action", ["Login", "Sign Up"])

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if action == "Login":
        if st.button("Login"):
            if login_user(username, password):
                st.session_state["user"] = username
                st.success(f"Welcome {username}!")
                return True
            else:
                st.error("Invalid credentials.")
    else:
        if st.button("Sign Up"):
            if register_user(username, password):
                st.success("User created! Please log in.")
            else:
                st.error("Username already exists.")
    return False
