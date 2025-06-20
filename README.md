# 📚 DocLearn – LangChain RAG App  
*Ask Smart Questions to Dumber PDFs!*

Tired of scrolling through entire PDFs like a caveman? Want to squeeze answers out of your boring documents like it's ChatGPT's job (because it literally is)?  
**DocLearn** turns your PDFs or text files into a Q&A machine using the magic of **RAG (Retrieval-Augmented Generation)**  so you can ask intelligent questions without doing intelligent work.

**Try out the app**
-[https://doclearn-sv.vercel.app](https://doclearn-sv.vercel.app)

---




## 🧠 Chain Architecture

RAG-based architecture using:  
- 🧾 **LangChain Loaders**: To load PDF/text 
- ✂️ **Recursive Text Splitter**: Breaks docs into bite-sized chunks  
- 🧠 **Google Gemini Embeddings**: Because I am too rich for OpenAI credits  
- 💾 **FAISS VectorDB**: Stores all the embeddings
- 🔗 **StuffDocumentsChain**: Actually merges info for the LLM to use  
- 🔍 **RetrievalChain**: So your questions go where they should, instead of screaming into the void  

---

## 📂 What It Looks Like
- Upload file  
- Ask question  
- Get response

---

## 🤡 Why This Exists?
Built this so I could actually understand langchain.

---

## 🛠️ Tech Stack
- **LangChain**  
- **FAISS**  
- **Gemini 2.0 flash (via Google Generative AI SDK)**  
- **HTML-CSS-JS**

---



