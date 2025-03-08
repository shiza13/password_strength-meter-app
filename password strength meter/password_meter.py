import streamlit as st
import os
import re

st.set_page_config(page_title="Password Strength Meter", page_icon="🔐", layout="centered")

password_file = os.path.join(os.path.dirname(__file__), "saved_passwords.txt")

st.markdown(
    """
    <style>
        body {
            background-color: #0cfedf;  /* Light Cyan */
        }
        .stApp {
            background-color: #0cfedf;  /* Light Cyan */
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<h1 style='text-align: center; color: #1438df;'>🔐 Password Strength Meter</h1>", unsafe_allow_html=True)
st.write("### Ensure your password is **strong and secure!**")

with st.expander("📌 **Password Requirements** (Click to View)"):
    st.markdown("""
    ✅ **At least one uppercase** letter (A-Z)  
    ✅ **At least one lowercase** letter (a-z)  
    ✅ **At least one number** (0-9)  
    ✅ **At least one special character** (!@#$%^&*)  
    ✅ **Length:** Adjustable **(9 to 18 characters)**
    """)

st.markdown("<h4>Select Password Length:</h4>", unsafe_allow_html=True)
password_length = st.slider("", min_value=9, max_value=18, value=12, help="Adjust password length")

st.markdown("<h4>Enter your Password:</h4>", unsafe_allow_html=True)
password = st.text_input("", type="password", placeholder="Type your password here...")

def check_password_strength(password):
    if len(password) < password_length:
        return "❌ Password too short!"
    if not re.search(r"[A-Z]", password):
        return "❌ Must contain at least one uppercase letter!"
    if not re.search(r"[a-z]", password):
        return "❌ Must contain at least one lowercase letter!"
    if not re.search(r"[0-9]", password):
        return "❌ Must contain at least one number!"
    if not re.search(r"[!@#$%^&*]", password):
        return "❌ Must contain at least one special character!"
    return "✅ Strong Password!"  

def save_password(password):
    try:
        with open(password_file, "a") as file:
            file.write(password + "\n")
        return True
    except Exception as e:
        st.error(f"⚠️ Error saving password: {e}")
        return False  

col1, col2 = st.columns(2)

with col1:
    if st.button("🔍 Check Password", use_container_width=True):
        strength_message = check_password_strength(password) 
        if "❌" in strength_message:
            st.error(strength_message)
        else:
            st.success(strength_message)

with col2:
    if st.button("📑 Save Password", use_container_width=True):
        strength_message = check_password_strength(password)  
        if "✅" in strength_message:
            if save_password(password):  
                st.success("✅ Password saved successfully!")
        else:
            st.warning("⚠️ Your password is weak. Improve it before saving.")

st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>👇 View Your Saved Passwords 👇</h4>", unsafe_allow_html=True)
st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)

if st.button("👁️ View Saved Passwords", use_container_width=True):
    st.switch_page("pages/save_password.py")

st.markdown("</div>", unsafe_allow_html=True)
st.markdown("<br><hr>", unsafe_allow_html=True)  
st.markdown("<h4 style='text-align: center; color: #666;'>✨ Created by Shiza Tariq😊 ✨</h4>", unsafe_allow_html=True)
