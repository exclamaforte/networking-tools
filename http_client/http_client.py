import fire
# HTTP client written using the Sockets API

def encode_string(s: str) -> bytes:
    """Encodes a string to send over a socket"""
    return s.encode("ISO-8859-1")

def decode_string(b: bytes) -> str:
    """Encodes a string to send over a socket"""
    return b.decode("ISO-8859-1")

def main():
    pass

if __name__ == '__main__':
    fire.Fire(main)

