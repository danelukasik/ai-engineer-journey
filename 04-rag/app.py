import streamlit as st
import chromadb
import anthropic
from dotenv import load_dotenv
import os
from pypdf import PdfReader

load_dotenv()
claude = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

def chunk_text(text, chunk_size=500, overlap=50):
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start += chunk_size - overlap
    return chunks

@st.cache_resource
def setup_rag():
    chroma_client = chromadb.Client()
    collection = chroma_client.get_or_create_collection(name="my_docs")

    if collection.count() == 0:  # only do the slow work if it hasn't been done yet
        reader = PdfReader("Spotify-2025-F-Filing.pdf")
        text = ""
        for page in reader.pages[:20]:
            text += page.extract_text()

        chunks = chunk_text(text)
        ids = [f"chunk_{i}" for i in range(len(chunks))]
        collection.add(documents=chunks, ids=ids)

    return collection

collection = setup_rag()

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

st.title("Spotify 10-K Q&A")
question = st.text_input("Ask a question about Spotify's SEC filing:")

if question:
    answer = ask_with_rag(question)
    st.write(answer)