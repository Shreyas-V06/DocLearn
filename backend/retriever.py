
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains.retrieval import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from backend.initialize_model import initialize_geminiLLM
from backend.loaders import LoadPrompt


def initialize_retriever(docs):
    text_splitter=RecursiveCharacterTextSplitter(chunk_size=100,chunk_overlap=30)
    chunks=text_splitter.split_documents(docs)
    embeddings=GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vectordb=FAISS.from_documents(chunks,embeddings)
    LLM=initialize_geminiLLM()
    prompt=LoadPrompt()
    document_chain=create_stuff_documents_chain(LLM,prompt)
    retriever=vectordb.as_retriever()
    qa_chain = create_retrieval_chain(retriever,document_chain)
    return qa_chain