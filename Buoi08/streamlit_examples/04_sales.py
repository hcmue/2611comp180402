import pandas as pd
import streamlit as st

st.set_page_config(page_title="Quản lý doanh thu", layout="wide")
st.title("Quản lý doanh thu bán hàng")
st.caption("Nhập đơn hàng, theo dõi doanh thu và xuất CSV.")

if "sales" not in st.session_state:
    st.session_state["sales"] = []

st.subheader("1. Nhập dữ liệu")
with st.form("sales_form", clear_on_submit=True):
    product = st.text_input("Tên sản phẩm")
    quantity = st.number_input("Số lượng", min_value=1, value=1, step=1)
    price = st.number_input("Đơn giá (VNĐ)", min_value=0, value=10000, step=1000)
    submitted = st.form_submit_button("Thêm sản phẩm")

if submitted:
    if not product.strip():
        st.warning("Vui lòng nhập tên sản phẩm.")
    else:
        st.session_state["sales"].append({
            "Sản phẩm": product.strip(),
            "Số lượng": quantity,
            "Đơn giá": price,
        })
        st.success("Đã thêm sản phẩm.")

if st.button("Xóa toàn bộ dữ liệu"):
    st.session_state["sales"] = []

st.subheader("2. Xem kết quả")
if not st.session_state["sales"]:
    st.info("Chưa có dữ liệu bán hàng.")
else:
    df = pd.DataFrame(st.session_state["sales"])
    df["Thành tiền"] = df["Số lượng"] * df["Đơn giá"]

    left, right = st.columns(2)
    with left:
        st.metric("Tổng số lượng", int(df["Số lượng"].sum()))
    with right:
        st.metric("Tổng doanh thu", f'{df["Thành tiền"].sum():,.0f} VNĐ')

    st.dataframe(df, hide_index=True)
    chart_data = df.groupby("Sản phẩm", as_index=False)["Thành tiền"].sum()
    st.bar_chart(chart_data, x="Sản phẩm", y="Thành tiền")

    csv_bytes = df.to_csv(index=False).encode("utf-8-sig")
    st.download_button(
        label="Tải dữ liệu CSV",
        data=csv_bytes,
        file_name="doanh_thu.csv",
        mime="text/csv",
    )
