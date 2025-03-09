import streamlit as st
import os

def delete_saved_passwords():
    """Deletes all saved passwords by clearing the file content."""
    try:
        password_file = os.path.join(os.path.dirname(__file__), "../saved_passwords.txt")
        if os.path.exists(password_file):
            with open(password_file, "w") as file:
                file.write("")  # Clear file content
        return True
    except Exception as e:
        st.error(f"Error deleting passwords: {e}")
        return False

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
    st.markdown("<h3 style='text-align: center;'>📋 Here you can see your all saved passwords:</h3>", unsafe_allow_html=True)
    st.markdown("<div class='password-container'>", unsafe_allow_html=True)

    for i, password in enumerate(passwords, 1):
        st.markdown(f"<div class='password-item'>{i}. {password.strip()}</div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)
else:
    st.warning("⚠️ No saved passwords found.")

# Delete passwords
if st.button("❌ Delete All Saved Passwords", use_container_width=True):
    if delete_saved_passwords():
        st.success("🗑️ All saved passwords have been deleted!")

# Download passwords
if os.path.exists(password_file):
    with open(password_file, "rb") as file:
        st.download_button(label="📥 Download Saved Passwords", data=file, file_name="saved_passwords.txt", mime="text/plain", use_container_width=True)

st.markdown("<br><hr>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: #666;'>✨ Created by Shiza Tariq 😊 ✨</h4>", unsafe_allow_html=True)
