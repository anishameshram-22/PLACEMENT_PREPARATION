import streamlit as st
import requests

st.set_page_config(page_title="PlacementPro AI")

st.title("🎯 PlacementPro AI")

# ---------------- LOGIN ---------------- #

if "token" not in st.session_state:

    st.subheader("Login")

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login", key="login_btn"):

        url = "http://127.0.0.1:5000/login"

        payload = {
            "email": email,
            "password": password
        }

        res = requests.post(url, json=payload)

        if res.status_code == 200:
            st.session_state["token"] = res.json()["token"]
            st.success("Login Successful")
        else:
            st.error("Invalid Credentials")

# ---------------- DASHBOARD ---------------- #

if "token" in st.session_state:

    st.success("Logged In Successfully")

    st.subheader("📊 Dashboard")

    col1, col2, col3 = st.columns(3)

    col1.metric("Questions Solved", 120)
    col2.metric("Coding Score", 85)
    col3.metric("Placement Readiness", "78%")

