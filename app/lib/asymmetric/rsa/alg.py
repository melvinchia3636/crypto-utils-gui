from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import pss
from Crypto.Hash import SHA256


KEY_SIZES = ["1024", "2048", "3072", "4096"]


def generate_keypair(
    size: int = 2048, passphrase: str | None = None
) -> tuple[str, str]:
    key = RSA.generate(size)
    pub = key.publickey().export_key().decode()
    priv = key.export_key(passphrase=passphrase, pkcs=8).decode()
    return pub, priv


def encrypt(pub_pem: str, plaintext: str) -> bytes:
    pubkey = RSA.import_key(pub_pem)
    cipher = PKCS1_OAEP.new(pubkey)
    return cipher.encrypt(plaintext.encode())


def decrypt(priv_pem: str, ciphertext: bytes, passphrase: str | None = None) -> str:
    privkey = RSA.import_key(priv_pem, passphrase=passphrase)
    cipher = PKCS1_OAEP.new(privkey)
    return cipher.decrypt(ciphertext).decode()


def sign(priv_pem: str, message: str, passphrase: str | None = None) -> bytes:
    privkey = RSA.import_key(priv_pem, passphrase=passphrase)
    h = SHA256.new(message.encode())
    return pss.new(privkey).sign(h)


def verify(pub_pem: str, message: str, signature: bytes) -> bool:
    pubkey = RSA.import_key(pub_pem)
    h = SHA256.new(message.encode())
    try:
        pss.new(pubkey).verify(h, signature)
        return True
    except (ValueError, TypeError):
        return False
