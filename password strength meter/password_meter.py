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
        input::placeholder {
            color: black;
            background-color: white;
            padding: 5px;
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
password = st.text_input("", type="password", placeholder="Enter your password here...")

def check_password_strength(password):
    strength = 0
    missing_requirements = []
    
    if len(password) >= password_length:
        strength += 1
    else:
        missing_requirements.append("Minimum length of " + str(password_length) + " characters")
    
    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        missing_requirements.append("At least one uppercase letter")
    
    if re.search(r"[a-z]", password):
        strength += 1
    else:
        missing_requirements.append("At least one lowercase letter")
    
    if re.search(r"[0-9]", password):
        strength += 1
    else:
        missing_requirements.append("At least one number")
    
    if re.search(r"[!@#$%^&*]", password):
        strength += 1
    else:
        missing_requirements.append("At least one special character")
    
    if strength == 5:
        return "✅ Strong Password!", strength, None
    elif strength >= 3:
        return "⚠️ Moderate Password", strength, missing_requirements
    else:
        return "❌ Weak Password", strength, missing_requirements

def save_password(password):
    try:
        with open(password_file, "a") as file:
            file.write(password + "\n")
        return True
    except Exception as e:
        st.error(f"⚠️ Error saving password: {e}")
        return False

def get_saved_passwords():
    if os.path.exists(password_file):
        with open(password_file, "r") as file:
            return file.readlines()
    return []

def delete_saved_passwords():
    try:
        os.remove(password_file)
        return True
    except Exception as e:
        st.error(f"⚠️ Error deleting passwords: {e}")
        return False

col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    if st.button("🔍 Check Password", use_container_width=True):
        strength_message, strength_level, missing_req = check_password_strength(password)
        if "❌" in strength_message:
            st.error(strength_message)
            if missing_req:
                st.warning("⚠️ Missing requirements: " + ", ".join(missing_req))
        elif "⚠️" in strength_message:
            st.warning(strength_message)
            if missing_req:
                st.info("ℹ️ Consider adding: " + ", ".join(missing_req))
        else:
            st.success(strength_message)
        
        st.progress(strength_level / 5)

with col2:
    if st.button("📑 Save Password", use_container_width=True):
        strength_message, strength_level, _ = check_password_strength(password)
        if "✅" in strength_message:
            if save_password(password):
                st.success("✅ Password saved successfully!")
        else:
            st.warning("⚠️ Your password is weak. Improve it before saving.")

with col3:
    if st.button("🔃Reset", use_container_width=True):
        st.session_state["password"] = ""  
        st.rerun() 

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("<h4 style='text-align: center;'>👇 You can see your saved passwords here 👇</h3>", unsafe_allow_html=True)
if st.button("👁️ View Saved Passwords", use_container_width=True):
    st.switch_page("pages/save_password.py")
    saved_passwords = get_saved_passwords()
    if saved_passwords:
        st.write("### 🔒 Your Saved Passwords:")
        for i, password in enumerate(saved_passwords, 1):
            st.text(f"{i}. {password.strip()}")
    else:
        st.warning("⚠️ No saved passwords found.")

st.markdown("<br><hr>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: #666;'>✨ Created by Shiza Tariq 😊 ✨</h4>", unsafe_allow_html=True)
