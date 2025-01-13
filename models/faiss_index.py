import faiss
import numpy as np

class FAISSIndex:
    def __init__(self, index_path="index.faiss"):
        self.index = faiss.read_index(index_path, faiss.IO_FLAG_MMAP | faiss.IO_FLAG_READ_ONLY)
        self.image_files = self.load_image_files("image_files.txt")

    def load_image_files(self, file_path):
        with open(file_path, "r") as f:
            return [line.strip() for line in f.readlines()]

    def search(self, embedding, top_k=5):
        embedding = embedding.astype("float32").reshape(1, -1)
        distances, indices = self.index.search(embedding, top_k)
        return [self.image_files[i] for i in indices[0]]
