## LangChain Chatbot with ChromaDB

### Description

This project implements a question-answering chatbot using the following components:

- LangChain for orchestrating the LLM and document retrieval
- ChromaDB as the vector database for storing and retrieving relevant documents
- Llama 3.2 as the underlying language model

The chatbot will:

1. Take user questions as input
2. Search the ChromaDB collection for relevant documents
3. Use LangChain to generate answers based on the retrieved documents
4. Provide source citations for the information used in the answers

### Technical Requirements

Core Dependencies:

- ChromaDB - Vector database for document storage and similarity search
- LangChain - Framework for LLM application development
- Llama 3.2 - Large language model (via Ollama)

Additional Requirements:

- Python 3.8+
- Sufficient RAM for running Llama 3.2
- Storage space for document embeddings

## Design
