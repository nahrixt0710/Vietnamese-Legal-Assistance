import os
from sentence_transformers import SentenceTransformer
import pinecone

# Load model
model = SentenceTransformer("sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")

# Init Pinecone
pinecone.init(api_key=os.getenv("PINECONE_API_KEY"), environment=os.getenv("PINECONE_ENV"))
index = pinecone.Index("legal-assistant")

def search_laws(query, top_k=5):
    # Chuyển câu hỏi thành embedding
    q_embedding = model.encode(query).tolist()

    # Tìm kiếm trong Pinecone
    result = index.query(
        vector=q_embedding,
        top_k=top_k,
        include_metadata=True
    )

    return result
