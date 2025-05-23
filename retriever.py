from sentence_transformers import SentenceTransformer
import faiss
import os

class DocumentRetriever:
    def __init__(self, docs_dir="docs"):
        self.docs = [open(os.path.join(docs_dir, f)).read() for f in os.listdir(docs_dir)]
        self.embedder = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')
        self.embeddings = self.embedder.encode(self.docs)
        self.index = faiss.IndexFlatL2(self.embeddings[0].shape[0])
        self.index.add(self.embeddings)

    def search(self, query, k=3):
        query_vec = self.embedder.encode([query])
        scores, indices = self.index.search(query_vec, k)
        return [self.docs[i] for i in indices[0]]
