from langchain_huggingface import HuggingFaceEmbeddings
from langchain_pinecone.vectorstores import PineconeVectorStore
from langchain_core.documents import Document
import os
from dotenv import load_dotenv
import logging

# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)

load_dotenv()

pinecone_api_key = os.getenv("PINECONE_API_KEY")
if not pinecone_api_key:
    raise ValueError("PINECONE_API_KEY is not set in the environment variables.")


embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
)


class CustomPineconeVectorStore(PineconeVectorStore):
    def _dict_to_document(self, pinecone_dict):
        # Map 'content' to 'page_content' and preserve other metadata
        text = pinecone_dict["metadata"].get("content", "")
        metadata = {k: v for k, v in pinecone_dict["metadata"].items() if k != "content"}
        return Document(page_content=text, metadata=metadata)


vectorstore = CustomPineconeVectorStore(
    index_name="vietnam-law-chatbot",
    embedding=embeddings,
    namespace="",
    pinecone_api_key=pinecone_api_key,
)

def search_laws(query, top_k=5):
    docs = vectorstore.similarity_search(query, k=top_k)
    return docs