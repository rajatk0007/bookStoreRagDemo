# src/vectorstore.py
import numpy as np

class VectorStore:
    def __init__(self, texts, embeddings, metadata):
        self.texts = texts
        self.embeddings = embeddings
        self.metadata = metadata

    def search(self, query_emb, top_k=3):
        """
        Return top_k most relevant books.
        """
        def cosine(u, v):
            return np.dot(u, v) / (np.linalg.norm(u) * np.linalg.norm(v) + 1e-10)

        scores = [cosine(query_emb, emb) for emb in self.embeddings]
        idxs = np.argsort(scores)[::-1][:top_k]
        return [self.metadata[i] for i in idxs if scores[i] > 0.5]
