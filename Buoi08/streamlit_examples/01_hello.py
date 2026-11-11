import streamlit as st

st.set_page_config(page_title="Ứng dụng đầu tiên")
st.title("Ứng dụng Streamlit đầu tiên")
st.write("Chào mừng bạn đến với Streamlit!")

name = st.text_input("Nhập họ tên:")
age = st.number_input("Nhập tuổi:", min_value=1, max_value=120, value=18)

if st.button("Xác nhận"):
    if name.strip():
        st.success(f"Xin chào {name.strip()}! Bạn {age} tuổi.")
    else:
        st.warning("Vui lòng nhập họ tên.")
