from Crypto.Hash import SHA256
from Crypto.Protocol.KDF import PBKDF2

DEFAULT_PASSPHRASE = "aVerySecretPassword@123"
DEFAULT_PLAINTEXT = "Hello World!\nThis text will be {actioned} by {cipher}.\nabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=[]{}|;':\",./<>?~`"


def derive_key(passphrase: str, key_bytes: int, salt: bytes = b"cryptofun") -> bytes:
    return PBKDF2(
        passphrase, salt, dkLen=key_bytes, count=100000, hmac_hash_module=SHA256
    )
