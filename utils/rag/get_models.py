from llama_index.llms.ollama import Ollama
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

from ..config import CONFIG


TEMPERATURE = CONFIG["TEMPERATURE"]
TIMEOUT = CONFIG["TIMEOUT"]


def get_embedding_model(embedding_model: str):
    embed_model = HuggingFaceEmbedding(model_name=embedding_model)
    return embed_model

def get_llm_model(llm_model: str, temp: float=TEMPERATURE, timeout: int=TIMEOUT):
    llm = Ollama(
        model=llm_model, 
        temperature=temp, 
        request_timeout=timeout)
    return llm
