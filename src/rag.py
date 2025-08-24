from src.vectorstore import VectorStore
from src.ingestion import load_books

class RAGPipeline:
    def __init__(self, store, llm):
        self.store = store
        self.llm = llm

    @classmethod
    def from_multiple_stores(cls, store_a_path, store_b_path, llm):
        books, embeddings = load_books(store_a_path, store_b_path)
        texts = [b['text'] for b in books]
        store = VectorStore(texts, embeddings, books)
        return cls(store, llm)

    def ask(self, query):
        from src.embeddings import generate_embeddings
        query_emb = generate_embeddings([query])[0]
        results = self.store.search(query_emb)
        if not results:
            return "No matching books found."
        # Return simple output
        output = []
        for r in results:
            output.append(f"{r['name']} by {r['author']} — {r['genre']}, costs {r['price']} at {r['store']}")
        return "\n".join(output)
