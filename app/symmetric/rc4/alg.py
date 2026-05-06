from Crypto.Cipher import ARC4


def encrypt(key: bytes, plaintext: str) -> bytes:
    cipher = ARC4.new(key)
    return cipher.encrypt(plaintext.encode())


def decrypt(key: bytes, ciphertext: bytes) -> str:
    cipher = ARC4.new(key)
    return cipher.decrypt(ciphertext).decode()
