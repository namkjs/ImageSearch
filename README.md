# **Search Image Web App**
## 🎥 Simple demo
![Recording 2025-01-13 103909](https://github.com/user-attachments/assets/741d3b3b-7d2e-4f3a-8525-88583a781e00)

***📖 Mô Tả Dự Án***

Ứng dụng web giúp tìm kiếm hình ảnh dựa trên mô tả văn bản hoặc hình ảnh đầu vào. Ứng dụng sử dụng mô hình CLIP để mã hóa dữ liệu và FAISS để tìm kiếm nhanh chóng.
## 👾 Tech Stack
<details>
  <summary>Technology</summary>
  <ul>
    <li>CNN</li>
    <li><a href="https://flask.palletsprojects.com/en/stable/">Flask</a></li>
    <li><a href="https://github.com/facebookresearch/faiss">FAISS</a></li>
    <li><a href="https://openai.com/index/clip/">CLIP</a></li>

  </ul>
</details>

***📂 Cấu Trúc Thư Mục***

![image](https://github.com/user-attachments/assets/724ae002-9630-440d-9e00-870d23b28d1a)


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

⚡ Tìm kiếm nhanh chóng nhờ FAISS Index.

