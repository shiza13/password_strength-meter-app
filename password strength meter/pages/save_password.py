import streamlit as st
import os

st.set_page_config(page_title="Saved Passwords", page_icon="🔒", layout="centered")

st.markdown(
    """
    <style>
        body {
            background-color: #0cfedf;  /* Light Cyan */
        }
        .stApp {
            background-color: #0cfedf;  /* Light Cyan */
        }
      
        .password-item {
            font-size: 16px;
            padding: 8px;
            margin: 5px 0;
            background-color: #f8f9fa;
            border-radius: 5px;
            border-left: 5px solid #4CAF50;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<h1 style='text-align: center; color: #1438df;'>🔒 Saved Passwords</h1>", unsafe_allow_html=True)

password_file = os.path.join(os.path.dirname(__file__), "../saved_passwords.txt")

if not os.path.exists(password_file):
    with open(password_file, "w") as file:
        pass  

with open(password_file, "r") as file:
    passwords = file.readlines()

if passwords:
    st.markdown("<h3 style='text-align: center;'>📋 Your Saved Passwords:</h3>", unsafe_allow_html=True)
    st.markdown("<div class='password-container'>", unsafe_allow_html=True)

    for i, password in enumerate(passwords, 1):
        st.markdown(f"<div class='password-item'>{i}. {password.strip()}</div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)
else:
    st.warning("⚠️ No saved passwords found.")
