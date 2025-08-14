# scripts/build_embeddings.py
import faiss
import pickle  # Use built-in pickle
from sentence_transformers import SentenceTransformer
from pathlib import Path

# Load SentenceTransformer model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Load all documents from data/documents/
docs_path = Path("data/documents/")
documents = [f.read_text(encoding="utf-8") for f in docs_path.glob("*.txt")]

# Encode documents to embeddings
embeddings = model.encode(documents)

# Create FAISS index
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

# Save FAISS index and documents
faiss.write_index(index, "data/embeddings.faiss")
with open("data/documents.pkl", "wb") as f:
    pickle.dump(documents, f)

print(f"✅ Built FAISS index with {len(documents)} documents")
