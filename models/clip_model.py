from sentence_transformers import SentenceTransformer
import torch
import os

class CLIPModel:
    def __init__(self, model_name='clip-ViT-B-32', model_path='saved_model'):
        device = 'cuda' if torch.cuda.is_available() else 'cpu'

        # Kiểm tra nếu mô hình đã tải về
        if not os.path.exists(model_path):
            print(f"🔽 Đang tải mô hình {model_name} ...")
            self.model = SentenceTransformer(model_name, device=device)
            self.model.save(model_path)  # Lưu lại mô hình
            print(f"✅ Đã lưu mô hình tại {model_path}")
        else:
            print(f"📂 Đang tải mô hình từ {model_path}")
            self.model = SentenceTransformer(model_path, device=device)

    def encode(self, data):
        return self.model.encode(data, convert_to_numpy=True, normalize_embeddings=True)
