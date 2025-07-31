import hashlib

def hash256(s: bytes) -> bytes:
    """
    Computes a double SHA-256 hash of the given input.

    This function applies the SHA-256 hash function twice to the input data,
    a common technique used in blockchain protocols (e.g., Bitcoin) for increased security.

    Args:
        s (bytes): The input data to be hashed.

    Returns:
        bytes: The resulting double SHA-256 hash as a bytes object.
    """
    return hashlib.sha256(hashlib.sha256(s).digest()).digest()
