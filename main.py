import os
import time
import streamlit as st
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import UnstructuredURLLoader
from langchain.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings

#from dotenv import load_dotenv
#load_dotenv()


# ✅ Set Gemini API key from Streamlit secrets
os.environ["GOOGLE_API_KEY"] = st.secrets["GOOGLE_API_KEY"]

# ✅ App Title
st.title("News Research Tool 📰")
st.sidebar.title("News Article URLs")

# ✅ Sidebar for entering URLs
urls = []
for i in range(3):
    url = st.sidebar.text_input(f"URL {i+1}")
    urls.append(url)

# ✅ Process URLs
process_url_clicked = st.sidebar.button("Process URLs")
main_placefolder = st.empty()

# ✅ LLM Setup (Gemini)
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.7)

if process_url_clicked and any(urls):
    try:
        # Load data
        loader = UnstructuredURLLoader(urls=urls)
        main_placefolder.text("🔄 Loading content from URLs...")
        data = loader.load()

        # Split content
        text_splitter = RecursiveCharacterTextSplitter(
            separators=['\n\n', '\n', '.', ','],
            chunk_size=1000
        )
        main_placefolder.text("✂️ Splitting text into chunks...")
        docs = text_splitter.split_documents(data)

        # Create embeddings and save FAISS index
        embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
        vectorized_index = FAISS.from_documents(docs, embeddings)

        main_placefolder.text("📦 Building and saving FAISS index...")
        vectorized_index.save_local("faiss_index")
        time.sleep(2)

        main_placefolder.success("✅ Documents processed! You can now ask a question.")
    except Exception as e:
        main_placefolder.error(f"❌ Error processing URLs: {str(e)}")

# ✅ Ask questions
query = main_placefolder.text_input("Question: ")

if query:
    try:
        embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
        vectorstore = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)

        chain = RetrievalQAWithSourcesChain.from_llm(llm=llm, retriever=vectorstore.as_retriever())
        result = chain({"question": query}, return_only_outputs=True)

        # Display answer
        st.header("Answer")
        st.write(result["answer"])

        # Display sources
        sources = result.get("sources", "")
        if sources:
            st.subheader("Sources:")
            for source in sources.split("\n"):
                st.write(source)

    except Exception as e:
        st.error(f"❌ Error during question answering: {str(e)}")

# Example URLs for testing:
# https://www.moneycontrol.com/news/business/tata-motors-mahindra-gain-certificates-for-production-linked-payouts-11281691.html
# https://www.moneycontrol.com/news/business/tata-motors-launches-punch-icng-price-starts-at-rs-7-1-lakh-11098751.html
# https://www.moneycontrol.com/news/business/stocks/buy-tata-motors-target-of-rs-743-kr-choksey-11080811.html
