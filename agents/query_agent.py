from langchain.chains import RetrievalQA
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from transformers import pipeline

# Load embeddings and models
embeddings = HuggingFaceEmbeddings()
vector_store = FAISS.load_local("path_to_index", embeddings)

qa = RetrievalQA.from_chain_type(
    llm=pipeline("text-generation"),
    retriever=vector_store.as_retriever()
)

def get_answer(query):
    return qa.run(query)
