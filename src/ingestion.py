import pandas as pd
from src.embeddings import generate_embeddings

def load_books(store_a_path, store_b_path):
    # Store A
    df_a = pd.read_csv(store_a_path)
    df_a = df_a.rename(columns={
        "title": "name",
        "writer": "author",
        "category": "genre",
        "price_inr": "price"
    })
    df_a['store'] = "Store A"

    # Store B
    df_b = pd.read_csv(store_b_path)
    df_b = df_b.rename(columns={
        "book_name": "name",
        "author_name": "author",
        "genre": "genre",
        "cost_usd": "price"
    })
    df_b['store'] = "Store B"

    # Combine
    df = pd.concat([df_a, df_b], ignore_index=True)

    # Text field for embeddings
    df['text'] = df.apply(lambda row: f"{row['name']} by {row['author']} — {row['genre']}, costs {row['price']} at {row['store']}", axis=1)

    books = df.to_dict(orient='records')
    embeddings = generate_embeddings(df['text'].tolist())
    return books, embeddings
