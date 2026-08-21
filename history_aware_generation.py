from dotenv import load_dotenv

from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage


# Load environment variables
load_dotenv()


# --------------------------------------------------
# Configuration
# --------------------------------------------------

persistent_directory = "db/chroma_db"

embedding_model_name = "sentence-transformers/all-MiniLM-L6-v2"

ollama_model = "llama3.2:3b"


# --------------------------------------------------
# Load Embeddings
# --------------------------------------------------

embeddings = HuggingFaceEmbeddings(
    model_name=embedding_model_name
)


# --------------------------------------------------
# Connect to ChromaDB
# --------------------------------------------------

db = Chroma(
    persist_directory=persistent_directory,
    embedding_function=embeddings
)


# --------------------------------------------------
# Set up Local AI Model
# --------------------------------------------------

model = ChatOllama(
    model=ollama_model,
    temperature=0
)


# --------------------------------------------------
# Store Conversation History
# --------------------------------------------------

chat_history = []


# --------------------------------------------------
# Ask Question
# --------------------------------------------------

def ask_question(user_question):

    print(f"\n--- You asked: {user_question} ---")


    # --------------------------------------------------
    # Step 1: Make the question standalone
    # --------------------------------------------------

    if chat_history:

        messages = [
            SystemMessage(
                content=(
                    "Given the conversation history, rewrite the new "
                    "question as a standalone question that can be "
                    "searched in a company knowledge base. "
                    "Return only the rewritten question."
                )
            )
        ] + chat_history + [
            HumanMessage(
                content=f"New question: {user_question}"
            )
        ]

        result = model.invoke(messages)

        search_question = result.content.strip()

        print(f"Searching for: {search_question}")

    else:

        search_question = user_question


    # --------------------------------------------------
    # Step 2: Retrieve Relevant Documents
    # --------------------------------------------------

    retriever = db.as_retriever(
        search_kwargs={"k": 3}
    )

    docs = retriever.invoke(search_question)

    print(f"Found {len(docs)} relevant documents:")


    for i, doc in enumerate(docs, 1):

        lines = doc.page_content.split("\n")[:2]

        preview = "\n".join(lines)

        print(f"  Doc {i}: {preview}...")


    # --------------------------------------------------
    # Step 3: Combine Retrieved Documents
    # --------------------------------------------------

    documents_text = "\n\n".join(
        [
            f"Document {i}:\n{doc.page_content}"
            for i, doc in enumerate(docs, 1)
        ]
    )


    # --------------------------------------------------
    # Step 4: Create Final Prompt
    # --------------------------------------------------

    combined_input = f"""
Answer the user's question using ONLY the information
contained in the provided documents.

User Question:
{user_question}

Documents:
{documents_text}

Rules:

1. Use only the provided documents.
2. Do not use outside knowledge.
3. Do not guess or invent information.
4. If the answer is not available in the documents, say:

"I don't have enough information to answer that question
based on the provided documents."

5. Give a clear and concise answer.
"""


    # --------------------------------------------------
    # Step 5: Generate Answer
    # --------------------------------------------------

    messages = [

        SystemMessage(
            content=(
                "You are a helpful company knowledge assistant. "
                "Answer questions using only the provided documents "
                "and the conversation context."
            )
        )

    ] + chat_history + [

        HumanMessage(
            content=combined_input
        )

    ]


    result = model.invoke(messages)

    answer = result.content


    # --------------------------------------------------
    # Step 6: Save Conversation
    # --------------------------------------------------

    chat_history.append(
        HumanMessage(content=user_question)
    )

    chat_history.append(
        AIMessage(content=answer)
    )


    # --------------------------------------------------
    # Display Answer
    # --------------------------------------------------

    print("\n--- Answer ---")

    print(answer)

    return answer


# --------------------------------------------------
# Chat Loop
# --------------------------------------------------

def start_chat():

    print("=" * 50)

    print(" Company RAG Chat Assistant ")

    print("=" * 50)

    print("Ask questions about Infosys, TCS, Accenture and Wipro.")

    print("Type 'quit' to exit.")


    while True:

        question = input("\nYour question: ")


        if question.lower().strip() == "quit":

            print("Goodbye!")

            break


        if not question.strip():

            print("Please enter a question.")

            continue


        ask_question(question)


# --------------------------------------------------
# Run Program
# --------------------------------------------------

if __name__ == "__main__":

    start_chat()