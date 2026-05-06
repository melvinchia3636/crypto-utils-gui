from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


def encrypt(key: bytes, plaintext: str) -> tuple[bytes, bytes, bytes]:
    nonce = get_random_bytes(12)
    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
    ct, tag = cipher.encrypt_and_digest(plaintext.encode())

    return nonce, ct, tag


def decrypt(key: bytes, nonce: bytes, ciphertext: bytes, tag: bytes) -> str:
    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)

    return cipher.decrypt_and_verify(ciphertext, tag).decode()
