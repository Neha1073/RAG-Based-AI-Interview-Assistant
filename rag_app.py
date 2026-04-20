import os
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.llms import Ollama
from langchain_ollama import OllamaLLM
from langchain_text_splitters import RecursiveCharacterTextSplitter

# =========================
# CONFIG
# =========================
DATA_PATH = "notes/"
INDEX_PATH = "faiss_index"
EMBED_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

USE_OLLAMA = True   # set False if using OpenAI

# =========================
# LOAD DOCUMENTS
# =========================
def load_documents():
    loader = DirectoryLoader(
        DATA_PATH,
        glob="**/*.md",
        loader_cls=TextLoader
    )
    documents = loader.load()
    print(f"Loaded {len(documents)} documents")
    return documents

# =========================
# SPLIT DOCUMENTS
# =========================
def split_documents(documents):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=400,
        chunk_overlap=100
    )
    docs = text_splitter.split_documents(documents)
    print(f"Created {len(docs)} chunks")
    return docs

# =========================
# CREATE VECTOR STORE
# =========================
def create_vectorstore(docs):
    embeddings = HuggingFaceEmbeddings(model_name=EMBED_MODEL)
    vectorstore = FAISS.from_documents(docs, embeddings)
    vectorstore.save_local(INDEX_PATH)
    print("Vector DB created and saved!")
    return vectorstore

# =========================
# LOAD VECTOR STORE
# =========================
def load_vectorstore():
    embeddings = HuggingFaceEmbeddings(model_name=EMBED_MODEL)
    vectorstore = FAISS.load_local(
    INDEX_PATH,
    embeddings,
    allow_dangerous_deserialization=True
)
    print("Vector DB loaded!")
    return vectorstore

# =========================
# LLM SETUP
# =========================
# def get_llm():
#     if USE_OLLAMA:
#         from langchain.llms import Ollama
#         return Ollama(model="tinyllama")  # make sure: ollama run mistral
#     else:
#         from langchain.chat_models import ChatOpenAI
#         return ChatOpenAI(
#             openai_api_key=os.getenv("OPENAI_API_KEY"),
#             model="gpt-3.5-turbo"
#         )
def get_llm():
    if USE_OLLAMA:
        from langchain_ollama import OllamaLLM
        return OllamaLLM(model="tinyllama")   # or mistral if it works
    else:
        from langchain_openai import ChatOpenAI
        return ChatOpenAI(model="gpt-3.5-turbo")
# =========================
# RAG QUERY
# =========================
def ask_question(vectorstore, query):
    retriever = vectorstore.as_retriever(search_kwargs={"k": 1})
    docs = retriever.invoke(query)

    context = "\n\n".join([doc.page_content for doc in docs])

    prompt = f"""
Answer the question using the context below.

Context:
{context}

Question:
{query}

Answer in one or two lines:
"""

    llm = get_llm()
    response = llm.invoke(prompt)

    print("\n===== ANSWER =====\n")
    print(response)

    print("\n===== SOURCES =====\n")
    for i, doc in enumerate(docs):
        print(f"{i+1}. {doc.metadata}")

# =========================
# MAIN
# =========================
def main():
    if not os.path.exists(INDEX_PATH):
        docs = load_documents()
        split_docs = split_documents(docs)
        vectorstore = create_vectorstore(split_docs)
    else:
        vectorstore = load_vectorstore()

    while True:
        query = input("\nAsk a question (or type 'exit'): ")
        if query.lower() == "exit":
            break
        ask_question(vectorstore, query)

if __name__ == "__main__":
    main()