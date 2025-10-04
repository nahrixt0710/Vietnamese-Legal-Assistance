# from langchain.chains import RetrievalQA
# from langchain.prompts import PromptTemplate
# from langchain.llms import HuggingFacePipeline
# from transformers import pipeline
# from langchain.schema import BaseRetriever, Document


# from src.retriever import search_laws 

# llm_pipeline = pipeline(
#     "text-generation",
#     model="google/flan-t5-small",
#     device=0,
#     max_new_tokens=100,
#     do_sample=True,
#     temperature=0.2
# )

# llm = HuggingFacePipeline(pipeline=llm_pipeline)

# class LawRetriever(BaseRetriever):
#     """Wrapper để dùng search_laws với LangChain"""
#     def get_relevant_documents(self, query: str):
#         results = search_laws(query)  
#         docs = []

#         for match in results:
#             if isinstance(match, Document):
#                 docs.append(match)
#             else:
#                 content = match.get("metadata", {}).get("content", "") or match.get("content", "")
#                 docs.append(Document(page_content=content, metadata=match.get("metadata", {})))
        
#         return docs

# retriever = LawRetriever()

# prompt_template = """
# Bạn là một trợ lý pháp lý. Dựa vào các văn bản luật dưới đây để trả lời câu hỏi.
# Nếu không tìm thấy thông tin phù hợp, hãy trả lời: "Tôi không tìm thấy trong luật."

# Văn bản luật:
# {context}

# Câu hỏi: {question}

# Trả lời:
# """

# PROMPT = PromptTemplate(
#     template=prompt_template,
#     input_variables=["context", "question"]
# )

# qa_chain = RetrievalQA.from_chain_type(
#     llm=llm,
#     chain_type="stuff", 
#     retriever=retriever,
#     return_source_documents=True,
#     chain_type_kwargs={"prompt": PROMPT}
# )

# def answer_question(query):
#     result = qa_chain({"query": query})
#     return result["result"]


from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain.llms import Ollama
from langchain.schema import BaseRetriever, Document
from src.retriever import search_laws


llm = Ollama(
    model="qwen2:7b",
    temperature=0.2
)

class LawRetriever(BaseRetriever):
    def get_relevant_documents(self, query: str):
        results = search_laws(query)
        docs = []
        for match in results:
            if isinstance(match, Document):
                docs.append(match)
            else:
                content = match.get("metadata", {}).get("content", "") or match.get("content", "")
                docs.append(Document(page_content=content, metadata=match.get("metadata", {})))
        return docs

retriever = LawRetriever()

prompt_template = """
Bạn là một trợ lý pháp lý. Dựa vào các văn bản luật dưới đây để trả lời câu hỏi.
Nếu không tìm thấy thông tin phù hợp, hãy trả lời: "Tôi không tìm thấy trong luật."

Văn bản luật:
{context}

Câu hỏi: {question}

Trả lời:
"""

PROMPT = PromptTemplate(
    template=prompt_template,
    input_variables=["context", "question"]
)

qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=retriever,
    return_source_documents=True,
    chain_type_kwargs={"prompt": PROMPT}
)

def answer_question(query):
    result = qa_chain({"query": query})
    return result["result"]
