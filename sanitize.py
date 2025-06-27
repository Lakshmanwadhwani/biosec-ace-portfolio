# sanitize.py
import re
DNA  = re.compile(r"[ACGT]{18,}", re.I)                # long DNA/RNA
STEP = re.compile(r"\b(step\s*\d{1,2}|procedure)\b", re.I)

def sanitize(text: str) -> str:
    """Remove obvious dual-use markers."""
    text = DNA.sub("[REDACTED_DNA]", text)
    text = STEP.sub("[REDACTED_STEP]", text)
    return text
