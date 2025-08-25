A simple Retrieval-Augmented Generation (RAG) pipeline built with Hugging Face Transformers and Gradio, that lets you query books across multiple stores — even if they use different schemas (e.g., Store A in INR, Store B in USD).

Features :
✅ Handles multiple bookstores with different CSV schemas
✅ Normalizes data (title/author/genre/price) into one consistent format
✅ Uses SentenceTransformers for semantic search
✅ Uses FLAN-T5 from Hugging Face as the reasoning LLM
✅ Gradio UI for asking questions interactively
✅ Simple, clear answers

Evidences :
<img width="1916" height="513" alt="image" src="https://github.com/user-attachments/assets/d2760a78-6f42-4e39-a12a-cbfdf4335f9b" />

<img width="1918" height="507" alt="evd_1 jpg" src="https://github.com/user-attachments/assets/23e7d8cb-4c8e-4040-8a18-e1918d31ee5f" />


Next Steps :
* Add currency conversion (USD ↔ INR) for fair price comparisons
 * Replace in-memory vector store with FAISS / Pinecone for scalability
 * Add filtering by genre / price range
 * Dockerize for easy deployment
