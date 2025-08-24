# app.py
import gradio as gr
from src.rag import RAGPipeline
from src.llm import hf_llm

STORE_A_CSV = "data/store_a.csv"
STORE_B_CSV = "data/store_b.csv"

print("📚 Loading data and initializing pipeline...")
rag = RAGPipeline.from_multiple_stores(STORE_A_CSV, STORE_B_CSV, llm=hf_llm)
print("✅ Pipeline ready!")

def answer_query(user_query):
    return rag.ask(user_query)

gr.Interface(
    fn=answer_query,
    inputs="text",
    outputs="text",
    title="Bookstore RAG",
    description="Ask questions about books across multiple stores."
).launch()
