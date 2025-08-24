from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

def generate_embeddings(texts):
    """
    Generate embeddings using Hugging Face model.
    """
    return model.encode(texts)
