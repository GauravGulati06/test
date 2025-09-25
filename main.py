from utils.rag.get_models import get_llm_model, get_gemini_llm , get_llm_model_hf , get_groq_llm
from rag import build_rag

llm = get_groq_llm()
response = build_rag(question="tell equations of mini batch gradient descent and stochastic gradient descent !",llm=llm)
print(response)