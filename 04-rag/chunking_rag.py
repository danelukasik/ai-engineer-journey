import chromadb
import anthropic
from dotenv import load_dotenv
import os

load_dotenv()
claude = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

chroma_client = chromadb.Client()
collection = chroma_client.create_collection(name="my_docs")

def chunk_text(text, chunk_size=500, overlap=50):
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start += chunk_size - overlap 
    return chunks

def ask_with_rag(question):
    results = collection.query(query_texts=[question], n_results=1)
    retrieved_text = results["documents"][0][0]

    prompt = f"""Answer the question using ONLY the context below. If the context doesn't contain the answer, say you don't know.

Context: {retrieved_text}

Question: {question}"""

    response = claude.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=300,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.content[0].text

from pypdf import PdfReader

reader = PdfReader("Spotify-2025-F-Filing.pdf")

text = ""
for page in reader.pages[:20]:   # just the first 20 pages
    text += page.extract_text()

chunks = chunk_text(text)
ids = [f"chunk_{i}" for i in range(len(chunks))]

collection.add(documents=chunks, ids=ids)

print(ask_with_rag("How much revenue did Spotify make in 2025?"))
print(ask_with_rag("How much revenue did Spotify make in 2026?"))