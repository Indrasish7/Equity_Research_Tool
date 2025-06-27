# 📰 Equity Research Tool

The Equity Research Tool is an AI-powered assistant that helps you analyze financial news articles and get source-backed answers to your queries — instantly.

> 🔗 **Live App**: [https://equityresearchtool7.streamlit.app](https://equityresearchtool7.streamlit.app)

---

## 🚀 Features

✅ Enter up to **3 financial article URLs**  
✅ Automatic **content extraction** and **chunking**  
✅ Text embedding via **Gemini’s `embedding-001` model**  
✅ Fast semantic search with **FAISS vector store**  
✅ Answer your questions using **Gemini 2.5 Flash**  
✅ **Source citations** included with each answer  
✅ Interactive and fast **Streamlit interface**

---

## 📸 Demo

_💡 Added a screenshot of the tool here for better understanding._
![image](https://github.com/user-attachments/assets/3dab61c0-1b87-4fd1-8ee0-85713cc991e9)


---

## 🧠 How It Works

1. Paste up to 3 financial news article URLs into the sidebar.
2. The tool scrapes content using `UnstructuredURLLoader` and splits it into chunks.
3. Gemini’s embedding model vectorizes the content.
4. FAISS creates a searchable index.
5. When you ask a question, the most relevant chunks are retrieved.
6. Gemini 2.5 Flash answers your question using the context.
7. Results are returned with proper source links.

---

## 💬 Example Questions

> "What is Tata Motors launching this quarter?"  
> "How are Mahindra and Tata benefitting from PLI?"  
> "What is the analyst recommendation on Tata stock?"
> "What is the price of Tiago iCNG?"
---

## ⚙️ Tech Stack

| Technology | Purpose |
|------------|---------|
| [Streamlit](https://streamlit.io) | Web interface |
| [LangChain](https://www.langchain.com/) | LLM pipelines |
| [Gemini API](https://makersuite.google.com/) | LLM & Embedding |
| [FAISS](https://github.com/facebookresearch/faiss) | Vector search |
| [Unstructured](https://github.com/Unstructured-IO/unstructured) | Web scraping |

---

## 📦 Installation (for Local Development)

```bash
git clone https://github.com/Indrasish7/equity_research_tool.git
cd equity_research_tool
pip install -r requirements.txt
