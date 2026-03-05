from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings

def create_vector_store(documents):

    embeddings = OpenAIEmbeddings()

    db = FAISS.from_texts(documents, embeddings)

    return db
