from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad


def encrypt(key: bytes, plaintext: str) -> tuple[bytes, bytes]:
    iv = get_random_bytes(8)
    cipher = DES.new(key, DES.MODE_CBC, iv=iv)
    ct = cipher.encrypt(pad(plaintext.encode(), 8))

    return iv, ct


def decrypt(key: bytes, iv: bytes, ciphertext: bytes) -> str:
    cipher = DES.new(key, DES.MODE_CBC, iv=iv)

    return unpad(cipher.decrypt(ciphertext), 8).decode()
