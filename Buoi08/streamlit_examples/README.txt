BỘ MÃ NGUỒN MẪU - BÀI HỌC STREAMLIT

Yêu cầu: Python 3.11-3.15, VS Code (tùy chọn).

1. Mở Terminal trong thư mục chứa các tệp.
2. Tạo môi trường: python -m venv .venv
3. Kích hoạt trên CMD: .venv\Scripts\activate.bat
4. Cài thư viện: python -m pip install -r requirements.txt
5. Chạy ví dụ: python -m streamlit run 01_hello.py
   Thay 01_hello.py bằng tên tệp tương ứng.

Ví dụ:
  01_hello.py: nhập thông tin và phản hồi.
  02_calculator.py: xử lý form và phép tính.
  03_counter.py: Session State.
  04_sales.py: doanh thu, bảng, biểu đồ, CSV.
  05_csv_dashboard.py: tải CSV và lọc dữ liệu.
  sample_sales.csv: dữ liệu mẫu cho ví dụ 05.

Lưu ý: session_state chỉ lưu theo phiên, không phải cơ sở dữ liệu.
