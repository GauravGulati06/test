import hashlib


def get_chunk_id(text: str, file_name: str, chunk_idx: int) -> str:
    """Generate a stable ID for each chunk (hash of file + chunk index)."""
    hash_digest = hashlib.md5(text.encode("utf-8")).hexdigest()[:8]
    return f"{file_name}_chunk{chunk_idx}_{hash_digest}"