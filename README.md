# test

## rag:

1. setup:
```bash
uv sync
```

2. ollama:
```bash
ollama serve
```

3. tracing:
```bash
uv run -m phoenix.server.main serve
```

4. run:
```bash
uv run rag.py
```


## task:

1. LLM returning an empty response, even when it was able to retrieve chunks & everything, why?
2. Use HF Inference API, instead of Ollama local model.
3. pytest?
4. Add re-ranker
5. FastAPI backend

---