from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS

'''STEP 4: Store Vector Embeddings into FAISS DB'''

def StoreEmbeddings(chunks):
    gemini_embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    VectorDB = FAISS.from_documents(chunks, gemini_embeddings)
    return VectorDB