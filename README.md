Company RAG Knowledge Assistant

A Retrieval-Augmented Generation (RAG) project that allows users to retrieve information from company knowledge documents using semantic search.

Currently, the knowledge base contains information about:

Infosys
TCS
Accenture
Wipro

The project uses local Hugging Face embeddings and ChromaDB, so the document embedding process does not require OpenAI API credits.

🚀 Project Architecture
Company Documents
       ↓
Document Loader
       ↓
Text Chunking
       ↓
Hugging Face Embeddings
       ↓
ChromaDB Vector Store
       ↓
User Query
       ↓
Semantic Retrieval
       ↓
Relevant Context
       ↓
LLM
       ↓
Final Answer
📁 Project Structure
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
├── venv/
│
├── ingestion_pipeline.py
├── retrieval_pipeline.py
├── requirements.txt
├── .gitignore
└── README.md
🛠️ Technologies Used
Python
LangChain
LangChain Community
LangChain HuggingFace
Hugging Face Sentence Transformers
ChromaDB
Python-dotenv
Git & GitHub
📄 Document Ingestion Pipeline

The ingestion pipeline performs three major tasks:

1. Document Loading

The system loads .txt files from the docs directory.

2. Text Splitting

Large documents are divided into smaller chunks so that they can be efficiently processed and searched.

3. Embeddings and Vector Storage

The project uses:

sentence-transformers/all-MiniLM-L6-v2

to convert text chunks into numerical embeddings.

These embeddings are stored in ChromaDB for semantic search.

🔍 Retrieval Pipeline

When a user enters a question:

User Question
      ↓
Create Query Embedding
      ↓
Search ChromaDB
      ↓
Retrieve Relevant Documents
      ↓
Return Context

For example:

Question:
What does Infosys do?

The system searches the vector database and retrieves the most relevant Infosys content.

💡 Example Questions

You can ask questions such as:

What does Infosys do?
When was TCS founded?
How many employees does Wipro have?
What technology areas does Accenture work in?
Which companies hire fresh graduates?
What skills are useful for Infosys technology roles?
Compare the services offered by TCS and Wipro.
⚙️ Installation
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
▶️ Run the Ingestion Pipeline

Make sure the company .txt files are inside:

docs/

Then run:

python ingestion_pipeline.py

This creates the ChromaDB vector store.

▶️ Run the Retrieval Pipeline

After ingestion is complete:

python retrieval_pipeline.py

The system can then retrieve relevant information from the company knowledge base
