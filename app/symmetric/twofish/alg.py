from . import twofishlib


def encrypt(key: bytes, plaintext: str) -> str:
    ct = twofishlib.encrypt(key, plaintext.encode())
    return ct.hex()


def decrypt(key: bytes, ciphertext_hex: str) -> str:
    ct = bytes.fromhex(ciphertext_hex)
    return twofishlib.decrypt(key, ct).decode()
