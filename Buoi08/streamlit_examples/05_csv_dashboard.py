import pandas as pd
import streamlit as st

st.set_page_config(page_title="CSV Dashboard", layout="wide")
st.title("Thống kê doanh thu từ tệp CSV")
st.caption("Tệp CSV cần có: Sản phẩm, Số lượng, Đơn giá.")

uploaded = st.file_uploader("Chọn tệp CSV", type="csv")
if uploaded is None:
    st.info("Hãy tải tệp sample_sales.csv để bắt đầu.")
    st.stop()

try:
    df = pd.read_csv(uploaded)
    required = {"Sản phẩm", "Số lượng", "Đơn giá"}
    if not required.issubset(df.columns):
        st.error("Tệp thiếu một trong các cột bắt buộc.")
        st.stop()
    df["Số lượng"] = pd.to_numeric(df["Số lượng"], errors="raise")
    df["Đơn giá"] = pd.to_numeric(df["Đơn giá"], errors="raise")
except (ValueError, UnicodeDecodeError, pd.errors.ParserError) as exc:
    st.error(f"Không đọc được dữ liệu hợp lệ: {exc}")
    st.stop()

if df.empty:
    st.warning("Tệp CSV không có dòng dữ liệu.")
    st.stop()

products = sorted(df["Sản phẩm"].dropna().astype(str).unique().tolist())
selected = st.multiselect("Lọc sản phẩm", products, default=products)
filtered = df[df["Sản phẩm"].astype(str).isin(selected)].copy()
filtered["Thành tiền"] = filtered["Số lượng"] * filtered["Đơn giá"]

st.metric("Doanh thu trong bộ lọc", f'{filtered["Thành tiền"].sum():,.0f} VNĐ')
st.dataframe(filtered, hide_index=True)
if not filtered.empty:
    chart_data = filtered.groupby("Sản phẩm", as_index=False)["Thành tiền"].sum()
    st.bar_chart(chart_data, x="Sản phẩm", y="Thành tiền")
else:
    st.info("Không có sản phẩm nào trong bộ lọc.")
