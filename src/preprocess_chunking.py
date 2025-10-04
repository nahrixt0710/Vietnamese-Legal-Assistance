import re
import json
from langchain.text_splitter import TextSplitter
from langchain_community.document_loaders import Docx2txtLoader

class LawArticleSplitter(TextSplitter):
    def split_text(self, text: str):
        pattern = r"(Điều\s+\d+[a-zA-Z]*)"
        parts = re.split(pattern, text)

        chunks = []
        current_article = ""
        for part in parts:
            if part.strip().startswith("Điều"):
                if current_article:
                    chunks.append(current_article.strip())
                current_article = part
            else:
                current_article += " " + part

        if current_article:
            chunks.append(current_article.strip())

        return chunks


def process_with_langchain(input_file, output_file="json/laws_chunks.json"):
    with open(input_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    splitter = LawArticleSplitter()

    processed = []
    for item in data:
        title = item["title"]
        content = item["text"]

        chunks = splitter.split_text(content)

        for i, chunk in enumerate(chunks):
            processed.append({
                "law": title,
                "article_id": f"{title}_dieu_{i+1}",
                "text": chunk
            })

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(processed, f, ensure_ascii=False, indent=2)

    print(f"Đã tách thành {len(processed)} chunks và lưu vào {output_file}")


if __name__ == "__main__":
    process_with_langchain("json/laws_data.json")
