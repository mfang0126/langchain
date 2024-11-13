from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

from langchain.schema import Document
from generate_mock_conversations import generate_mock_conversations

# Initialize the embedding model with explicit model name
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")

# Generate mock conversations
mock_conversations = generate_mock_conversations(10)

# Convert mock conversations to Documents
documents = [
    Document(
        page_content=conv['content'],
        metadata=conv['metadata']
    ) for conv in mock_conversations
]

# Create a Chroma vector store
vectorstore = Chroma.from_documents(
    documents,
    embedding=embeddings,
    persist_directory="./chroma_db"
)