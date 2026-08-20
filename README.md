Company RAG Knowledge Assistant

A Retrieval-Augmented Generation (RAG) application that retrieves relevant information from company knowledge documents using semantic search.

Current Knowledge Base
Infosys
TCS
Accenture
Wipro
Overview

This project demonstrates how RAG can be used to retrieve relevant information from a collection of company documents.

The system:

Loads company documents
Splits documents into smaller chunks
Converts chunks into vector embeddings
Stores embeddings in ChromaDB
Converts user queries into embeddings
Retrieves the most relevant document chunks
Architecture
Company Documents
        ↓
Document Loading
        ↓
Text Splitting
        ↓
Hugging Face Embeddings
        ↓
ChromaDB
        ↓
User Query
        ↓
Semantic Retrieval
        ↓
Relevant Context
Technologies Used
Technology	Purpose
Python	Application development
LangChain	RAG pipeline
Hugging Face	Local text embeddings
Sentence Transformers	Embedding model
ChromaDB	Vector database
Python-dotenv	Environment configuration
Git & GitHub	Version control
Embedding Model
sentence-transformers/all-MiniLM-L6-v2

The embedding model runs locally, so the document embedding stage does not require OpenAI API credits.
Project Structure
RAG/
│
├── docs/
│   ├── infosys.txt
│   ├── tcs.txt
│   ├── accenture.txt
│   └── wipro.txt
│
├── db/
│   └── chroma_db/
│
├── ingestion_pipeline.py
├── retrieval_pipeline.py
├── requirements.txt
├── .gitignore
└── README.md
Setup
1. Clone the Repository
git clone https://github.com/YOUR_USERNAME/company-rag-chatbot.git
cd company-rag-chatbot
2. Create a Virtual Environment

For Windows:

python -m venv venv

Activate the virtual environment:

.\venv\Scripts\Activate.ps1
3. Install Dependencies
pip install -r requirements.txt

Run the Project
Step 1: Create the Vector Database

Place the company .txt files inside the docs folder.

Run:

python ingestion_pipeline.py

This will:

Load the company documents
Split the documents into chunks
Generate local embeddings
Store the embeddings in ChromaDB
Step 2: Run Retrieval
python retrieval_pipeline.py

You can then enter questions related to the information stored in the company knowledge base.

Example Queries
What does Infosys do?
When was TCS founded?
How many employees does Wipro have?
What technology areas does Accenture work in?
What skills are useful for Infosys technology roles?
Compare TCS and Wipro.
Key Features
Document-based information retrieval
Semantic document search
Local embedding generation
Persistent ChromaDB vector store
Multiple company knowledge sources
Easy to extend with additional companies
