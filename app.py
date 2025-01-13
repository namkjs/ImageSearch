from flask import Flask, request, render_template, send_from_directory
from googletrans import Translator
import os
from models.clip_model import CLIPModel
from models.faiss_index import FAISSIndex
from models.image_search import ImageSearch

app = Flask(__name__)

# ➡️ Thêm User-Agent không chuẩn để bỏ qua cảnh báo Ngrok
@app.before_request
def modify_user_agent():
    request.headers.environ['HTTP_USER_AGENT'] = "CustomUserAgent/1.0"

# Load model và FAISS index
clip_model = CLIPModel()
faiss_index = FAISSIndex()
image_search = ImageSearch(clip_model, faiss_index)

# Khởi tạo Translator để dịch tiếng Việt sang tiếng Anh
translator = Translator()

# Hàm dịch tiếng Việt sang tiếng Anh
def translate_to_english(text):
    try:
        translated = translator.translate(text, src='vi', dest='en')
        return translated.text
    except Exception as e:
        print(f"Lỗi dịch: {e}")
        return text  # Nếu lỗi, giữ nguyên text

# Trang chủ
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

# Tìm kiếm (kết hợp dịch tiếng Việt)
@app.route('/search', methods=['POST'])
def search():
    text = request.form.get('text')
    results = []

    if text:
        # Dịch tiếng Việt sang tiếng Anh
        translated_text = translate_to_english(text)
        print(f"Từ khóa sau khi dịch: {translated_text}")

        # Tìm kiếm bằng văn bản đã dịch
        results = image_search.search_by_text(translated_text)

    return render_template('results.html', images=results)

# Route để phục vụ ảnh
@app.route('/images/<path:filename>')
def serve_image(filename):
    folder = os.path.dirname(filename)
    file = os.path.basename(filename)
    return send_from_directory(folder, file)

if __name__ == "__main__":
    app.run()