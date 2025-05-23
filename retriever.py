from sentence_transformers import SentenceTransformer
import faiss
import os

embed_model = SentenceTransformer('sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2')

docs = [open(f'docs/{f}').read() for f in os.listdir('docs')]
doc_embeddings = embed_model.encode(docs)

index = faiss.IndexFlatL2(doc_embeddings[0].shape[0])
index.add(doc_embeddings)

def search(query):
    query_vec = embed_model.encode([query])
    scores, indices = index.search(query_vec, k=3)
    return [docs[i] for i in indices[0]]
