from llama_index.core import SimpleDirectoryReader
import sys
from exception import customexception
from logger import logging
import tempfile
import os

def load_data(uploaded_file):
    """
    Load document from uploaded file.

    Parameters:
    - uploaded_file: StreamlitUploadedFile object containing the document

    Returns:
    - A list containing the loaded document
    """
    try:
        logging.info("data loading started...")
        
        if uploaded_file is None:
            raise ValueError("No file uploaded")
            
        # Create a temporary directory
        with tempfile.TemporaryDirectory() as temp_dir:
            # Save uploaded file to temporary directory
            temp_file_path = os.path.join(temp_dir, uploaded_file.name)
            with open(temp_file_path, "wb") as f:
                f.write(uploaded_file.getbuffer())
            
            # Load the document from temporary directory
            loader = SimpleDirectoryReader(temp_dir)
            documents = loader.load_data()
            
        logging.info("data loading completed...")
        return documents
        
    except Exception as e:
        logging.info("exception in loading data...")
        raise customexception(e, sys)