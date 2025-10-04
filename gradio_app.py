import gradio as gr
from src.qa import answer_question

# Hàm chatbot cho Gradio
def chatbot(message, history):
    return answer_question(message)

# Tạo giao diện Gradio
demo = gr.ChatInterface(fn=chatbot, title="Legal Assistant Chatbot")

if __name__ == "__main__":
    demo.launch()
