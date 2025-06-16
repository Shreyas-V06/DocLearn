import os
import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI

def initialize_geminiLLM():
    gemini_api_key=os.getenv('GOOGLE_API_KEY')
    genai.configure(api_key=gemini_api_key)
    gemini_llm=ChatGoogleGenerativeAI(model="gemini-2.0-flash")
    return gemini_llm


