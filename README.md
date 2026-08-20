Company RAG Knowledge Assistant

A Retrieval-Augmented Generation (RAG) application that retrieves relevant information from company knowledge documents using semantic search.

The current knowledge base contains information about:

Infosys
TCS
Accenture
Wipro
Overview

This project demonstrates how RAG can be used to retrieve relevant information from a collection of documents.

The system:

Loads company documents.
Splits documents into smaller chunks.
Converts chunks into vector embeddings.
Stores embeddings in ChromaDB.
Converts a user's query into an embedding.
Retrieves the most relevant document chunks.
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
Technologies
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
1. Clone the repository
git clone https://github.com/YOUR_USERNAME/company-rag-chatbot.git
cd company-rag-chatbot
2. Create a virtual environment

Windows:

python -m venv venv

Activate it:

.\venv\Scripts\Activate.ps1
3. Install dependencies
pip install -r requirements.txt
Run the Project
Create the Vector Database

Place the company .txt files inside the docs folder and run:

python ingestion_pipeline.py

This loads the documents, creates chunks, generates embeddings and stores them in ChromaDB.

Run Retrieval
python retrieval_pipeline.py

You can then enter questions related to the information stored in the company documents.

Example Queries
What does Infosys do?

When was TCS founded?

How many employees does Wipro have?

What technology areas does Accenture work in?

What skills are useful for Infosys technology roles?

Compare TCS and Wipro.
Key Features
Document-based question answering foundation
Semantic document retrieval
Local embedding generation
Persistent ChromaDB vector store
Multiple company knowledge sources
Easy to extend with additional companies
Future Enhancements
Integrate an LLM for final answer generation
Build a web-based chatbot interface
Support PDF and DOCX documents
Allow users to upload their own documents
Add source citations
Add conversation history
Add company comparison functionality
Add retrieval evaluation
