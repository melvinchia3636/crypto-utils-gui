from Crypto.Cipher import AES as AES_Cipher
from Crypto.Random import get_random_bytes
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives.kdf.hkdf import HKDF

KEY_SIZES = ["2048", "3072", "4096"]


def generate_params(key_size: int = 2048) -> dh.DHParameters:
    return dh.generate_parameters(generator=2, key_size=key_size)


def params_to_pem(params: dh.DHParameters) -> str:
    return params.parameter_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.ParameterFormat.PKCS3,
    ).decode()


def params_from_pem(pem: str) -> dh.DHParameters:
    return serialization.load_pem_parameters(pem.encode())


def generate_keypair(params: dh.DHParameters) -> tuple[str, str]:
    priv = params.generate_private_key()
    pub = priv.public_key()

    return export_pub_key(pub), export_priv_key(priv)


def export_pub_key(pub) -> str:
    return pub.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo,
    ).decode()


def export_priv_key(priv) -> str:
    return priv.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption(),
    ).decode()


def import_pub_key(pem: str):
    return serialization.load_pem_public_key(pem.encode())


def import_priv_key(pem: str):
    return serialization.load_pem_private_key(pem.encode(), password=None)


def compute_shared_secret(priv, pub) -> tuple[bytes, bytes]:
    shared = priv.exchange(pub)
    derived = HKDF(
        algorithm=hashes.SHA256(),
        length=32,
        salt=None,
        info=b"dh-key-agreement",
    ).derive(shared)

    return shared, derived


def aes_gcm_encrypt(key: bytes, plaintext: str) -> tuple[bytes, bytes, bytes]:
    nonce = get_random_bytes(12)
    cipher = AES_Cipher.new(key, AES_Cipher.MODE_GCM, nonce=nonce)
    ct, tag = cipher.encrypt_and_digest(plaintext.encode())

    return nonce, ct, tag


def aes_gcm_decrypt(key: bytes, nonce: bytes, ciphertext: bytes, tag: bytes) -> str:
    cipher = AES_Cipher.new(key, AES_Cipher.MODE_GCM, nonce=nonce)

    return cipher.decrypt_and_verify(ciphertext, tag).decode()
