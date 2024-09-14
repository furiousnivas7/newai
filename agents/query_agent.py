from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from transformers import pipeline

# Load embeddings and models
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
# Allow dangerous deserialization since we trust our pickle file source
vector_store = FAISS.load_local("path_to_index", embeddings, allow_dangerous_deserialization=True)

qa = RetrievalQA.from_chain_type(llm=pipeline("text-generation"), retriever=vector_store.as_retriever())

def retrieve_answer(query):
    return qa.run(query)
