from docx import Document
import os
import json

def extract_text_from_docx(docx_path):
    """
    Đọc nội dung file Word (.docx) và trả về text
    """
    doc = Document(docx_path)
    all_text = []
    for para in doc.paragraphs:
        if para.text.strip():
            all_text.append(para.text.strip())
    return "\n".join(all_text)


def process_folder(docx_folder, output_file="laws_data.json"):
    """
    Đọc tất cả file Word trong thư mục và lưu ra JSON
    """
    data = []
    for filename in os.listdir(docx_folder):
        if filename.endswith(".docx"):
            path = os.path.join(docx_folder, filename)
            print(f"Đang xử lý: {filename}")
            
            text = extract_text_from_docx(path)
            law_data = {
                "file": filename,
                "title": filename.replace(".docx", ""),
                "content": text
            }
            data.append(law_data)
    
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Đã lưu dữ liệu {len(data)} file Word vào {output_file}")


if __name__ == "__main__":
    docx_folder = "data"  
    process_folder(docx_folder)
