from langchain.text_splitter import RecursiveCharacterTextSplitter

'''STEP 3: Split documents into chunks'''

def SplitDocument(docs):
    text_splitter=RecursiveCharacterTextSplitter(chunk_size=100,chunk_overlap=30)
    chunks=text_splitter.split_documents(docs)
    return chunks

