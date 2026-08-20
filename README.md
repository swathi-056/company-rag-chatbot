Company RAG Knowledge Assistant

A simple Retrieval-Augmented Generation (RAG) project that retrieves relevant information from company documents using semantic search.

The current knowledge base contains information about:

Infosys
TCS
Accenture
Wipro
Overview

The project loads company documents, splits them into smaller chunks, converts the text into vector embeddings, stores the embeddings in ChromaDB, and retrieves relevant information based on a user's query.

Workflow
Company Documents
        ↓
Document Loading
        ↓
Text Splitting
        ↓
Local Embeddings
        ↓
ChromaDB
        ↓
User Query
        ↓
Semantic Retrieval
        ↓
Relevant Documents
Technologies Used
Python
LangChain
Hugging Face
Sentence Transformers
ChromaDB
Python-dotenv
Git & GitHub
Embedding Model
sentence-transformers/all-MiniLM-L6-v2

The embedding model runs locally, so OpenAI API credits are not required for document embedding.

Installation
1. Clone the repository
git clone https://github.com/YOUR_USERNAME/company-rag-chatbot.git
cd company-rag-chatbot
2. Create a virtual environment
python -m venv venv

Activate it on Windows:

.\venv\Scripts\Activate.ps1
3. Install dependencies
pip install -r requirements.txt
Usage

Place the company .txt files in the docs folder.

Run the ingestion pipeline:

python ingestion_pipeline.py

This loads the documents, creates chunks, generates embeddings, and stores them in ChromaDB.

Then run the retrieval pipeline:

python retrieval_pipeline.py

You can ask questions related to the information contained in the company documents.

Example Questions
What does Infosys do?
When was TCS founded?
How many employees does Wipro have?
What technology areas does Accenture work in?
What skills are useful for Infosys technology roles?
Compare TCS and Wipro.
Current Features
Company document loading
Text chunking
Local embedding generation
ChromaDB vector storage
Semantic retrieval
Multiple company knowledge sources
