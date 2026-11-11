import streamlit as st

st.set_page_config(page_title="Máy tính đơn giản")
st.title("Máy tính hai số")

with st.form("calculator_form"):
    a = st.number_input("Số a", value=0.0)
    b = st.number_input("Số b", value=0.0)
    operation = st.selectbox("Phép tính", ["Cộng", "Trừ", "Nhân", "Chia"])
    submitted = st.form_submit_button("Tính kết quả")

if submitted:
    if operation == "Cộng":
        result = a + b
    elif operation == "Trừ":
        result = a - b
    elif operation == "Nhân":
        result = a * b
    elif b == 0:
        result = None
        st.error("Không thể chia cho 0.")
    else:
        result = a / b

    if result is not None:
        st.success(f"Kết quả: {result:g}")
