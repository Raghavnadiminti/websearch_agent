from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document

embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
vector_store = Chroma(collection_name="my_collection", embedding_function=embeddings)


def add_docs(documents):
    valid_docs = []

    for i, doc in enumerate(documents):
        if isinstance(doc, Document):
            valid_docs.append(doc)
        

    if not valid_docs:
        
        return "No valid documents were added."

    vector_store.add_documents(valid_docs)
    print("Documents added successfully.")
    return "Documents added successfully."


retriever = vector_store.as_retriever(search_kwargs={"k": 3})


def retrieve(query):
    docs = retriever.invoke(query)
    combined_text = "\n\n".join([doc.page_content for doc in docs])
    return combined_text
