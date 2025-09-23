from pathlib import Path
import chromadb

from llama_index.core import (
    SimpleDirectoryReader,
    VectorStoreIndex,
    Settings,
    StorageContext,
)
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.core.node_parser import SentenceSplitter

from utils.config import CONFIG
from utils.rag.get_models import get_embedding_model, get_llm_model
from utils.rag.get_prompt import RESPONSE_SYNTHESIS_PROMPT

import phoenix as px
from openinference.instrumentation.llama_index import LlamaIndexInstrumentor
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk import trace as trace_sdk
from opentelemetry.sdk.trace.export import SimpleSpanProcessor


# configs
DATA_DIR = Path(CONFIG["DATA_DIR"])
CHROMA_DIR = Path(CONFIG["CHROMA_DIR"])
CHROMA_COLLECTION = CONFIG["CHROMA_COLLECTION"]

EMBEDDING_MODEL = CONFIG["EMBEDDING_MODEL"]
LLM_MODEL = CONFIG["LLM_MODEL"]

CHUNK_SIZE = CONFIG["CHUNK_SIZE"]
CHUNK_OVERLAP = CONFIG["CHUNK_OVERLAP"]
TOP_K = CONFIG["TOP_K"]

QUERY = CONFIG["QUERY"]

# tracing
endpoint = "http://localhost:6006/v1/traces"
tracer_provider = trace_sdk.TracerProvider()
tracer_provider.add_span_processor(SimpleSpanProcessor(OTLPSpanExporter(endpoint)))
LlamaIndexInstrumentor().instrument(tracer_provider=tracer_provider)


def build_rag():
    # 1. Load PDF/DOC/TXT documents
    docs = SimpleDirectoryReader(DATA_DIR).load_data()

    # 2. Split docs into chunks
    splitter = SentenceSplitter(chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP)
    nodes = splitter.get_nodes_from_documents(docs)

    # 3. Setup embedding + LLM
    embed_model = get_embedding_model(embedding_model=EMBEDDING_MODEL)
    llm = get_llm_model(llm_model=LLM_MODEL)

    # 4. Setup persistent Chroma client
    chroma_client = chromadb.PersistentClient(path=CHROMA_DIR)
    chroma_collection = chroma_client.get_or_create_collection(CHROMA_COLLECTION)
    vector_store = ChromaVectorStore(chroma_collection=chroma_collection)

    # 5. Wrap vector_store with StorageContext
    storage_context = StorageContext.from_defaults(vector_store=vector_store)

    # 6. Apply global settings
    Settings.llm = llm
    Settings.embed_model = embed_model

    # 7. Build or update index
    index = VectorStoreIndex(
        nodes,
        storage_context=storage_context,
    )

    # 8. Define a custom prompt
    qa_template = RESPONSE_SYNTHESIS_PROMPT

    # 9. Create query engine with prompt
    query_engine = index.as_query_engine(
        text_qa_template=qa_template,
        similarity_top_k=TOP_K,
    )

    # 10. Run a query
    response = query_engine.query(QUERY)
    
    
    print("\n=== RESPONSE ===\n")
    print(response)
    
    print("\n=== RETRIEVED CHUNKS ===\n")
    for i, node in enumerate(response.source_nodes, 1):
        print(f"Chunk {i}:")
        print(node.node.get_content())  # the actual text
        print("-" * 60)


if __name__ == "__main__":
    build_rag()
