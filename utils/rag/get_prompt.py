from llama_index.core import PromptTemplate


RESPONSE_SYNTHESIS_PROMPT = PromptTemplate(
    """
    You are an expert research analyst.
    
    Below is the context information:
    ---------------------
    {context_str}
    ---------------------
    
    Given the context information and not prior knowledge, answer the question as best you can.
    Question: {query_str}
    
    Answer in 2-3 sentences only.
    """
    )