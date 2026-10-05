import streamlit as st

from src.screens.home_screen import home_screen


def main():
    st.set_page_config(
        page_title="Face Recognition Based Biometric Attendance System",
        page_icon="📷"
    )

    if "login_type" not in st.session_state:
        st.session_state["login_type"] = None

    if st.session_state["login_type"] == "student":
        student_screen()
    else:
        home_screen()


main()