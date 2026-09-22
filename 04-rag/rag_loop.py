import chromadb
import anthropic
from dotenv import load_dotenv
import os

load_dotenv()
claude = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

chroma_client = chromadb.Client()
collection = chroma_client.create_collection(name="my_docs")

collection.add(
    documents=[
        "The company's return policy allows returns within 30 days of purchase.",
        "Our office is located in Denver, Colorado.",
        "Employees get 15 days of paid time off per year."
    ],
    ids=["doc1", "doc2", "doc3"]
)

def ask_with_rag(question):
    # 1. Retrieve the most relevant document
    results = collection.query(query_texts=[question], n_results=1)
    retrieved_text = results["documents"][0][0]

    # 2. Build a prompt that includes the retrieved context
    prompt = f"""Answer the question using ONLY the context below. If the context doesn't contain the answer, say you don't know.

Context: {retrieved_text}

Question: {question}"""

    # 3. Ask Claude, grounded in that context
    response = claude.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=300,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.content[0].text

print(ask_with_rag("How many vacation days do I get?"))
print(ask_with_rag("What's your return policy?"))
print(ask_with_rag("Do you offer free shipping?"))