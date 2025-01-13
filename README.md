# **Search Image Web App**

***📖 Mô Tả Dự Án***

Ứng dụng web giúp tìm kiếm hình ảnh dựa trên mô tả văn bản hoặc hình ảnh đầu vào. Ứng dụng sử dụng mô hình CLIP để mã hóa dữ liệu và FAISS để tìm kiếm nhanh chóng.

***📂 Cấu Trúc Thư Mục***

SEARCHIMAGE/
├── models/               # Chứa các mô hình AI
├── saved_model/          # Mô hình đã tải (tự động lưu sau khi chạy)
├── static/               # File tĩnh (JS, CSS)
│   ├── main.js
│   └── style.css
├── templates/           # Giao diện HTML
│   ├── index.html       # Trang chủ
│   └── results.html     # Hiển thị kết quả tìm kiếm
├── .gitignore           # File loại trừ khi push lên GitHub
├── app.py               # Chạy Flask server
├── image_files.txt      # Lưu danh sách file ảnh
├── index.faiss          # FAISS index để tìm kiếm
├── README.md            # Hướng dẫn sử dụng
├── requirements.txt     # Thư viện cần cài đặt
├── vercel.json          # Cấu hình deploy với Vercel
└── ViT.ipynb            # Tải và tạo mô hình trước khi chạy server

***⚙️ Cài Đặt***

1. Clone Dự Án

git clone https://github.com/namkjs/ImageSearch.git
cd search_image

2. Cài Đặt Thư Viện

pip install -r requirements.txt

3. Chạy Notebook để Tải Mô Hình

Chạy file ViT.ipynb để tải và lưu mô hình vào thư mục saved_model/.

4. Chạy Flask App

python app.py

🔗 Truy cập http://127.0.0.1:5000 trên trình duyệt để sử dụng ứng dụng.

***🚀 Tính Năng***

🔍 Tìm kiếm hình ảnh bằng văn bản (hỗ trợ tiếng Việt).

📷 Tìm kiếm hình ảnh bằng ảnh tải lên.

![Recording 2025-01-13 103909](https://github.com/user-attachments/assets/741d3b3b-7d2e-4f3a-8525-88583a781e00)

⚡ Tìm kiếm nhanh chóng nhờ FAISS Index.
