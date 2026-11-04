# Chạy website Python Journey

Ứng dụng Streamlit tổng hợp lộ trình 15 tuần, hiển thị README/notes/mã nguồn của từng tuần và cung cấp phòng thực hành tương tác.

## Chạy trên máy tính

Yêu cầu Python 3.12 trở lên.

```bash
git clone https://github.com/MulSuLinh/python-journey.git
cd python-journey
python -m venv .venv
```

Kích hoạt môi trường ảo:

```powershell
# Windows PowerShell
.venv\Scripts\Activate.ps1
```

```bash
# macOS/Linux
source .venv/bin/activate
```

Cài thư viện và chạy web:

```bash
python -m pip install -r requirements.txt
streamlit run app.py
```

Trình duyệt thường tự mở tại `http://localhost:8501`.

## Đưa website lên Internet bằng Streamlit Community Cloud

1. Đẩy repository lên GitHub.
2. Mở https://share.streamlit.io/ và đăng nhập bằng GitHub.
3. Chọn **Create app**.
4. Chọn repository `MulSuLinh/python-journey`.
5. Chọn branch `upgrade/python-journey-v2` (hoặc branch đã merge app).
6. Đặt **Main file path** là `app.py`.
7. Chọn **Deploy**.

Ứng dụng chỉ đọc các tệp Markdown/Python có sẵn trong repository để hiển thị. Các file bài tập được trình bày dưới dạng mã nguồn, không tự động thực thi file tùy ý.
