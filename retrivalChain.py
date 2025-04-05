from langchain.chains import create_retrieval_chain

'''STEP 7: Create the retrieval chain'''

def LoadRetrievalChain(VectorDB,document_chain):
    retriever=VectorDB.as_retriever()
    retrieval_chain=create_retrieval_chain(retriever,document_chain)
    return retrieval_chain