import chromadb

client = chromadb.Client()
collection = client.create_collection(name="my_docs")

collection.add(
    documents=[
        "The company's return policy allows returns within 30 days of purchase.",
        "Our office is located in Denver, Colorado.",
        "Employees get 15 days of paid time off per year."
    ],
    ids=["doc1", "doc2", "doc3"]
)

results = collection.query(
    query_texts=["How many vacation days do I get?"],
    n_results=1
)

print(results)