from langchain_core.prompts import ChatPromptTemplate
from langchain_community.document_loaders import PyPDFLoader,TextLoader

def LoadPDFDocument(address):
    loader=PyPDFLoader(address)
    docs=loader.load()
    return docs
def LoadTextDocument(address):
    loader=TextLoader(address)
    docs=loader.load()
    return docs

def LoadPrompt():
    prompt= ChatPromptTemplate.from_template("""
Answer the following question based on the context mentioned below:
                                          
<context>
{context}
</context>
                                          
Question: {input}""")
    return prompt