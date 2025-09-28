import json
import os

from sentence_transformers import SentenceTransformer
from pinecone import Pinecone, ServerlessSpec
from dotenv import load_dotenv

# ==== 1. Khởi tạo Pinecone client ====
load_dotenv()
api_key = os.getenv("PINECONE_API_KEY")

pc = Pinecone(api_key=api_key)

index_name = "vietnam-law-chatbot"

# Tạo index nếu chưa tồn tại
if index_name not in pc.list_indexes().names():
    pc.create_index(
        name=index_name,
        dimension=384,   # kích thước vector (phụ thuộc model embedding)
        metric="cosine",
        spec=ServerlessSpec(cloud="aws", region="us-east-1")
    )

index = pc.Index(index_name)

# ==== 2. Load mô hình embedding ====
model = SentenceTransformer("sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")

# ==== 3. Load dữ liệu luật đã chunk ====
with open("laws_chunks.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# ==== 4. Tạo embeddings và insert vào Pinecone ====
vectors = []
for item in data:
    vector = model.encode(item["content"]).tolist()
    vectors.append({
        "id": item["article_id"],   # ID duy nhất
        "values": vector,           # vector embedding
        "metadata": {
            "law": item["law"],
            "content": item["content"]
        }
    })

# Insert batch vào Pinecone
index.upsert(vectors=vectors)

print(f"Đã lưu {len(vectors)} chunks vào Pinecone index '{index_name}'")
