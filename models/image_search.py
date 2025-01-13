from PIL import Image
import numpy as np

class ImageSearch:
    def __init__(self, clip_model, faiss_index):
        self.clip_model = clip_model
        self.faiss_index = faiss_index

    def search_by_text(self, text):
        embedding = self.clip_model.encode(text)
        return self.faiss_index.search(embedding)

    def search_by_image(self, image_path):
        image = Image.open(image_path).convert("RGB")
        embedding = self.clip_model.encode(image)
        return self.faiss_index.search(embedding)
