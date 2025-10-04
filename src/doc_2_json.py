from langchain_community.document_loaders import Docx2txtLoader
import os
import json

def process_folder_with_langchain(docx_folder, output_file="json/laws_data.json"):
    data = []
    for filename in os.listdir(docx_folder):
        if filename.endswith(".docx"):
            path = os.path.join(docx_folder, filename)
            print(f"Đang xử lý: {filename}")
            
            loader = Docx2txtLoader(path)
            documents = loader.load()
            
            content = "\n".join([doc.page_content for doc in documents])
            
            law_data = {
                "file": filename,
                "title": filename.replace(".docx", ""),
                "text": content
            }
            data.append(law_data)
    
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Đã lưu dữ liệu {len(data)} file Word vào {output_file}")


if __name__ == "__main__":
    docx_folder = "./data"
    process_folder_with_langchain(docx_folder)
