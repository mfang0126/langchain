from langchain.retrievers import ContextualCompressionRetriever
from langchain.retrievers.document_compressors import LLMChainExtractor
from langchain_ollama import OllamaLLM

from chroma_store import vectorstore

# Create a basic retriever
retriever = vectorstore.as_retriever()

# Create a contextual compression retriever for better results
llm = OllamaLLM(model="llama3.2", temperature=0)
compressor = LLMChainExtractor.from_llm(llm)
compression_retriever = ContextualCompressionRetriever(
    base_compressor=compressor,
    base_retriever=retriever
)

# Function to perform retrieval with metadata filtering
def retrieve_conversations(query, metadata_filter=None, k=5):
    if metadata_filter:
        results = compression_retriever.get_relevant_documents(
            query,
            filter=metadata_filter,
            search_kwargs={"k": k}
        )
    else:
        results = compression_retriever.get_relevant_documents(query, search_kwargs={"k": k})
    
    return results

# Example usage
query = "What are the product inquiries?"
metadata_filter = {"conversation_topic": "product inquiry"}
results = retrieve_conversations(query, metadata_filter)

# Print results with confidence scores
for doc in results:
    print(f"Content: {doc.page_content}")
    print(f"Metadata: {doc.metadata}")
    print(f"Confidence Score: {doc.metadata.get('confidence_score', 'N/A')}")
    print("---")