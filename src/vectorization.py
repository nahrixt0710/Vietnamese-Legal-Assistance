from langchain_huggingface import HuggingFaceEmbeddings
from pinecone import Pinecone, ServerlessSpec
import os, json
from dotenv import load_dotenv

load_dotenv()
pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
index_name = "vietnam-law-chatbot"

if index_name not in pc.list_indexes().names():
    pc.create_index(
        name=index_name,
        dimension=384,
        metric="cosine",
        spec=ServerlessSpec(cloud="aws", region="us-east-1")
    )

index = pc.Index(index_name)

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
)

with open("laws_chunks.json", "r", encoding="utf-8") as f:
    data = json.load(f)

vectors = []
for item in data:
    vector = embeddings.embed_query(item["text"])
    vectors.append({
        "id": item["article_id"],
        "values": vector,
        "metadata": {
            "law": item["law"],
            "text": item["text"]
        }
    })

index.upsert(vectors=vectors)
