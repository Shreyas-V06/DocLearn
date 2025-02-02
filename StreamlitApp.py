import streamlit as st
from DocChat.data_ingestion import load_data
from DocChat.embedding import download_gemini_embedding
from DocChat.model_api import load_model

def main():
    # Page configuration
    st.set_page_config(
        page_title="DocLearn",
        page_icon="📚",
        layout="centered",
        initial_sidebar_state="collapsed"
    )
    
    # Custom CSS for dark theme styling
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
    
    # Header with minimal styling
    st.markdown("<h1 style='color: #FAFAFA;'>📚 DocLearn</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='color: #C2C2C2;'>Your AI-Powered Document Learning Assistant</h3>", unsafe_allow_html=True)
    
    # Create two columns for better layout
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("<h4 style='color: #C2C2C2;'>Upload Your Document</h4>", unsafe_allow_html=True)
        doc = st.file_uploader("", type=['pdf', 'txt'])
        
    with col2:
        st.markdown("<h4 style='color: #C2C2C2;'>Supported Formats</h4>", unsafe_allow_html=True)
        st.markdown("<p style='color: #A0A0A0;'>• PDF files (.pdf)<br>• Text files (.txt)</p>", unsafe_allow_html=True)
    
    # Subtle divider
    st.markdown("<hr style='border: 1px solid #262730;'>", unsafe_allow_html=True)
    
    # Question input
    st.markdown("<h4 style='color: #C2C2C2;'>Ask Your Question</h4>", unsafe_allow_html=True)
    user_question = st.text_input("", placeholder="Type your question here...")
    
    # Submit button
    if st.button("🔍 Get Answer"):
        if doc is None:
            st.error("📁 Please upload a document first!")
            return
            
        if not user_question:
            st.error("❓ Please enter a question!")
            return
            
        with st.spinner("Analyzing your document..."):
            try:
                document = load_data(doc)
                model = load_model()
                query_engine = download_gemini_embedding(model, document)
                
                response = query_engine.query(user_question + "\nFormat your answer properly by including newline characters")
                
                # Display response in a dark themed box
                st.markdown("<h4 style='color: #C2C2C2;'>💡 Answer</h4>", unsafe_allow_html=True)
                st.markdown(f"""
                    <p style='background-color: #262730; 
                             padding: 20px; 
                             border-radius: 4px;
                             border: 1px solid #4B4B4B;
                             color: #FAFAFA;
                             margin: 10px 0;'>
                    {response.response}
                    </p>
                """, unsafe_allow_html=True)
                
            except Exception as e:
                st.error(f"⚠️ An error occurred: {str(e)}")
    
    # Footer
    st.markdown("<hr style='border: 1px solid #262730;'>", unsafe_allow_html=True)
    st.markdown("""
        <div style='text-align: center; color: #666;'>
        Made with ❤️ by DocLearn Team (Sohan, Shreyas and Saahil)
        </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()          