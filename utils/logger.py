import logging
import sys
import io


def setup_logger(name: str):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Prevent adding multiple handlers on re-imports
    if not logger.handlers:
        # Remove any existing handlers to prevent duplicates
        if logger.hasHandlers():
            logger.handlers.clear()
        
        formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(name)s: %(message)s")
        
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')  # Force UTF-8 console output
        
        ch = logging.StreamHandler(sys.stdout)
        ch.setFormatter(formatter)        
        logger.addHandler(ch)

    return logger