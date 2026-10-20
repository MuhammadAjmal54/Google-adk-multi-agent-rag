
# rag_setup.py

import os
import chromadb
import ollama


# ============================================
# OLLAMA EMBEDDING FUNCTION
# ============================================
class OllamaEmbeddingFunction:
    """Custom embedding function using Ollama nomic-embed-text."""

    def __init__(self, model_name="nomic-embed-text"):
        self.model_name = model_name

    def name(self) -> str:
        return f"ollama-{self.model_name}"

    def embed_query(self, input: list[str]) -> list[list[float]]:
        """Generate embeddings for query texts."""
        return self.embed_documents(input)

    def embed_documents(self, input: list[str]) -> list[list[float]]:
        """Generate embeddings for document or query texts."""
        embeddings = []

        for text in input:
            response = ollama.embeddings(
                model=self.model_name,
                prompt=text
            )
            embeddings.append(response["embedding"])

        return embeddings

    def __call__(self, input: list[str]) -> list[list[float]]:
        """Support ChromaDB versions that call the embedding function."""
        return self.embed_documents(input)



# ============================================
# CHUNKING FUNCTION
# ============================================
def chunk_text(text, chunk_size=500, chunk_overlap=100):
    """Split text into chunks with overlap."""

    paragraphs = text.split("\n\n")
    chunks = []
    current_chunk = ""

    for para in paragraphs:
        para = para.strip()

        if not para:
            continue

        if len(current_chunk) + len(para) + 2 <= chunk_size:
            current_chunk += para + "\n\n"
        else:
            if current_chunk.strip():
                chunks.append(current_chunk.strip())

            if chunk_overlap > 0 and len(current_chunk) > chunk_overlap:
                overlap_text = current_chunk[-chunk_overlap:]
                current_chunk = overlap_text + para + "\n\n"
            else:
                current_chunk = para + "\n\n"

    if current_chunk.strip():
        chunks.append(current_chunk.strip())

    return chunks


# ============================================
# MAIN RAG SETUP
# ============================================
def setup_rag():
    print("Setting up RAG with ChromaDB...")

    # Resolve paths relative to this Python file.
    project_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(project_dir, "data")
    db_path = os.path.join(data_dir, "chroma_db")

    # Ensure the data directory exists.
    os.makedirs(data_dir, exist_ok=True)

    # Persistent ChromaDB client.
    client = chromadb.PersistentClient(path=db_path)

    # Embedding function.
    embedding_fn = OllamaEmbeddingFunction(
        model_name="nomic-embed-text"
    )

    # Delete the old collection if it exists.
    try:
        client.delete_collection("company_knowledge")
        print("Deleted old collection.")
    except Exception:
        pass

    # Create a fresh collection.
    collection = client.create_collection(
        name="company_knowledge",
        embedding_function=embedding_fn,
        metadata={
            "description": "Company policies and FAQs"
        }
    )

    print("Created new collection.")

    # ----------------------------------------
    # Read company policies.
    # ----------------------------------------
    policies_path = os.path.join(
        data_dir, "company_policies.txt"
    )

    with open(policies_path, "r", encoding="utf-8") as file:
        policies_text = file.read()

    policies_chunks = chunk_text(
        policies_text,
        chunk_size=500,
        chunk_overlap=100
    )

    documents = []

    for i, chunk in enumerate(policies_chunks):
        documents.append({
            "id": f"policy_{i}",
            "text": chunk,
            "metadata": {
                "source": "company_policies",
                "chunk_id": i
            }
        })

    # ----------------------------------------
    # Read company FAQs.
    # ----------------------------------------
    faqs_path = os.path.join(
        data_dir, "company_faqs.txt"
    )

    with open(faqs_path, "r", encoding="utf-8") as file:
        faqs_text = file.read()

    faqs_chunks = chunk_text(
        faqs_text,
        chunk_size=500,
        chunk_overlap=100
    )

    for i, chunk in enumerate(faqs_chunks):
        documents.append({
            "id": f"faq_{i}",
            "text": chunk,
            "metadata": {
                "source": "company_faqs",
                "chunk_id": i
            }
        })

    if not documents:
        print("No document chunks found. Nothing to index.")
        return collection

    # ----------------------------------------
    # Insert documents into ChromaDB.
    # ----------------------------------------
    ids = [doc["id"] for doc in documents]
    texts = [doc["text"] for doc in documents]
    metadatas = [doc["metadata"] for doc in documents]

    print(f"Adding {len(documents)} chunks to vector DB...")
    print("Generating embeddings through Ollama...")

    collection.add(
        ids=ids,
        documents=texts,
        metadatas=metadatas
    )

    print("\nRAG setup complete!")
    print(f"Total chunks stored: {len(documents)}")
    print(f"Policy chunks: {len(policies_chunks)}")
    print(f"FAQ chunks: {len(faqs_chunks)}")
    print(f"Vector DB location: {db_path}")

    # ----------------------------------------
    # Test similarity search.
    # ----------------------------------------
    print("\nTesting similarity search...")

    results = collection.query(
        query_texts=["What is the leave policy?"],
        n_results=min(2, collection.count())
    )

    print("Test query: 'What is the leave policy?'")

    if results["documents"] and results["documents"][0]:
        print("Top result:")
        print(results["documents"][0][0][:300])
    else:
        print("No results returned.")

    return collection


# ============================================
# RUN SCRIPT
# ============================================
if __name__ == "__main__":
    setup_rag()
