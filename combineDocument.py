from langchain.chains.combine_documents import create_stuff_documents_chain

'''STEP 6: Create stuff documents chain'''

def CreateStuffDocChain(LLM,prompt):
    document_chain=create_stuff_documents_chain(LLM,prompt)
    return document_chain