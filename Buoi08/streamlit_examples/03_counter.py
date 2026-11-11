import streamlit as st

st.set_page_config(page_title="Bộ đếm")
st.title("Bộ đếm với Session State")

if "count" not in st.session_state:
    st.session_state["count"] = 0

if st.button("Tăng 1"):
    st.session_state["count"] += 1

if st.button("Đặt lại"):
    st.session_state["count"] = 0

st.metric("Giá trị hiện tại", st.session_state["count"])
