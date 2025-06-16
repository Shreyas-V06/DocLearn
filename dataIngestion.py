from langchain_community.document_loaders import PyPDFLoader,TextLoader

'''STEP 2: Data Ingestion'''

def LoadPDFDocument(pdf_address):
    loader=PyPDFLoader(pdf_address)
    docs=loader.load()
    return docs

def LoadTextDocument(text_address):
    loader=TextLoader(text_address)
    docs=loader.load()
    return docs


