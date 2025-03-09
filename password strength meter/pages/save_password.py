import streamlit as st
import os

if "passwords_deleted" not in st.session_state:
    st.session_state.passwords_deleted = False

def delete_saved_passwords():
    try:
        password_file = os.path.join(os.path.dirname(__file__), "../saved_passwords.txt")
        if os.path.exists(password_file):
            with open(password_file, "w") as file:
                file.write("")
        st.session_state.passwords_deleted = True
    except Exception as e:
        st.error(f"Error deleting passwords: {e}")

st.set_page_config(page_title="Saved Passwords", page_icon="🔒", layout="centered")

st.markdown(
    """
    <style>
        body {
            background-color: #0cfedf;
        }
        .stApp {
            background-color: #0cfedf;
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

if not st.session_state.passwords_deleted:
    with open(password_file, "r") as file:
        passwords = file.readlines()
else:
    passwords = []

if passwords:
    st.markdown("<h3 style='text-align: center;'>📋 Here you can see your saved passwords:</h3>", unsafe_allow_html=True)
    st.markdown("<div class='password-container'>", unsafe_allow_html=True)

    for i, password in enumerate(passwords, 1):
        st.markdown(f"<div class='password-item'>{i}. {password.strip()}</div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)
else:
    st.warning("⚠️ No saved passwords found.")

if st.button("❌ Delete All Saved Passwords", use_container_width=True):
    delete_saved_passwords()
    st.rerun()

if passwords:
    with open(password_file, "rb") as file:
        st.download_button(label="📥 Download Saved Passwords", data=file, file_name="saved_passwords.txt", mime="text/plain", use_container_width=True)

st.markdown("<br><hr>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: #666;'>✨ Created by Shiza Tariq 😊 ✨</h4>", unsafe_allow_html=True)
