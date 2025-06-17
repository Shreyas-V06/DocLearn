from backend.retriever import initialize_retriever
from backend.loaders import LoadPDFDocument,LoadTextDocument
from fastapi import FastAPI,UploadFile,File,Form
from fastapi.middleware.cors import CORSMiddleware
import tempfile
app=FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post('/uploadfile')
def query_file(user_question:str=Form(...),uploaded_file:UploadFile=File(...)):

    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        tmp_file.write(uploaded_file.file.read())
        file_path = tmp_file.name
    if uploaded_file.filename.endswith(".pdf"):
        docs = LoadPDFDocument(file_path)
    elif uploaded_file.filename.endswith(".txt"):
        docs = LoadTextDocument(file_path)
    else:
        return {"error":"Invalid file type"}
    
    retriever=initialize_retriever(docs)
    response = retriever.invoke({"input": user_question})
    return {"answer":response['answer']}

        
    