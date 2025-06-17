import streamlit as st
import tempfile
from backend.loaders import LoadPDFDocument,LoadTextDocument
from retriever import initialize_retriever

st.set_page_config(
        page_title="DocLearn",
        page_icon="📚",
        layout="centered",
        initial_sidebar_state="collapsed"
    )

st.markdown("""
        <style>
        .main {
            background-color: #0E1117;
            padding: 2rem;
        }
        .stButton>button {
            width: 100%;
            border-radius: 4px;
            height: 3em;
            background-color: #262730;
            color: #FAFAFA;
            border: 1px solid #4B4B4B;
        }
        .stButton>button:hover {
            border-color: #6B6B6B;
            background-color: #363740;
        }
        .stTextInput>div>div>input {
            border-radius: 4px;
            background-color: #262730;
            color: #FAFAFA;
            border: 1px solid #4B4B4B;
        }
        .css-1d391kg {
            background-color: #262730;
        }
        div[data-testid="stFileUploadDropzone"] {
            background-color: #262730;
            border: 1px solid #4B4B4B;
        }
        </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 style='color: #FAFAFA;'>📚 DocLearn</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='color: #C2C2C2;'> RAG Powered QA system</h3>", unsafe_allow_html=True)



uploaded_file = st.file_uploader("Upload a PDF or TXT file", type=["pdf", "txt"])

if uploaded_file:
    
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        tmp_file.write(uploaded_file.read())
        file_path = tmp_file.name

    
    if uploaded_file.name.endswith(".pdf"):
        docs = LoadPDFDocument(file_path)
    elif uploaded_file.name.endswith(".txt"):
        docs = LoadTextDocument(file_path)
    else:
        st.write("Invalid File type")

    retriever=initialize_retriever(docs)
    user_question = st.text_input("Ask your question about the document")

    if user_question:
        with st.spinner("Analyzing document... 🤖"):
            response = retriever.invoke({"input": user_question})
            st.markdown(response['answer'])