# 🇻🇳 Vietnamese Legal Assistance Chatbot

**Vietnamese Legal Assistance** là chatbot hỗ trợ tư vấn pháp luật cơ bản cho người dùng Việt Nam.  
Hiện tại, hệ thống tập trung vào **luật Hôn nhân và Gia đình**, giúp người dùng dễ dàng tra cứu và hiểu các quy định pháp luật liên quan đến kết hôn, ly hôn, quyền và nghĩa vụ của vợ chồng, nuôi con, tài sản chung – riêng, v.v.

---

## Công nghệ sử dụng

Dự án được xây dựng dựa trên các công cụ mạnh mẽ và hiện đại trong lĩnh vực AI và NLP:

- **LangChain** – quản lý pipeline và chuỗi truy vấn RAG (Retrieval-Augmented Generation)  
- **Pinecone** – cơ sở dữ liệu vector dùng để lưu trữ và tìm kiếm ngữ nghĩa (semantic search)  
- **Ollama** – nền tảng chạy mô hình ngôn ngữ nội bộ (LLM) như Qwen, LLaMA, Mistral...  
- **Gradio** – tạo giao diện web tương tác đơn giản để trò chuyện với chatbot  

---

## Hướng dẫn cài đặt và chạy chatbot

### Cài đặt Ollama
Truy cập trang chủ **[https://ollama.ai](https://ollama.ai)** để tải và cài đặt Ollama phù hợp với hệ điều hành của bạn (Windows, macOS hoặc Linux).

---

### Tải mô hình ngôn ngữ
Mở **Command Prompt (CMD)** hoặc **Terminal** và chạy lệnh sau để tải mô hình Qwen 2:
```bash
ollama pull qwen2:7b
```

---

### Tạo Pinecone API
Truy cập trang https://www.pinecone.io. Tạo tài khoản và vào API Keys để lấy API Key.

Tạo file .env trong thư mục gốc của project (cùng cấp với gradio_app.py), sau đó thêm nội dung sau:
```bash
PINECONE_API_KEY=your_pinecone_api_key_here
```
---

### Chạy ứng dụng Gradio
Sau khi tải mô hình xong, chạy chatbot bằng lệnh:
```bash
python gradio_app.py
```

Ứng dụng sẽ tự động mở giao diện web (thường tại địa chỉ: http://127.0.0.1:7860) để bạn có thể trò chuyện với chatbot.