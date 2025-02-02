import streamlit as st
from DocChat.data_ingestion import load_data
from DocChat.embedding import download_gemini_embedding
from DocChat.model_api import load_model

    
def main():
    st.set_page_config("DocChat")
    
    doc=st.file_uploader("Upload your Document")
    
    st.header("DocChat (Chat with your Documents!)")
    
    user_question= st.text_input("Ask any question about your document")
    
    if st.button("Submit & Ask"):
        with st.spinner("Processing..."):
            document=load_data(doc)
            model=load_model()
            query_engine=download_gemini_embedding(model,document)
                
            response = query_engine.query(user_question + "\nFormat your answer properly by including newline characters")
                
            st.write(response.response)
                
                
if __name__=="__main__":
    main()          
                
    
    
    
    
    