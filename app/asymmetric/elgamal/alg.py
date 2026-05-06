from Crypto.PublicKey import ElGamal as _ElGamal
from Crypto import Random
from Crypto.Hash import SHA256
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES
from base64 import b64encode, b64decode


KEY_SIZES = ["256", "512", "1024", "2048"]


def generate_keypair(key_size: int = 256) -> tuple[str, str]:
    key = _ElGamal.generate(key_size, Random.new().read)
    pub_pem = _serialize_pub(int(key.p), int(key.g), int(key.y))
    priv_pem = _serialize_priv(int(key.p), int(key.g), int(key.y), int(key.x))
    return pub_pem, priv_pem


def _serialize_pub(p, g, y):
    bl = (p.bit_length() + 7) // 8
    lines = ["-----BEGIN ELGAMAL PUBLIC KEY-----"]
    lines.append(b64encode(p.to_bytes(bl)).decode())
    lines.append(b64encode(g.to_bytes(bl)).decode())
    lines.append(b64encode(y.to_bytes(bl)).decode())
    lines.append("-----END ELGAMAL PUBLIC KEY-----")
    return "\n".join(lines)


def _serialize_priv(p, g, y, x):
    bl = (p.bit_length() + 7) // 8
    lines = ["-----BEGIN ELGAMAL PRIVATE KEY-----"]
    lines.append(b64encode(p.to_bytes(bl)).decode())
    lines.append(b64encode(g.to_bytes(bl)).decode())
    lines.append(b64encode(y.to_bytes(bl)).decode())
    lines.append(b64encode(x.to_bytes(bl)).decode())
    lines.append("-----END ELGAMAL PRIVATE KEY-----")
    return "\n".join(lines)


def _import_pub(pem: str):
    lines = pem.strip().splitlines()
    if lines[0] != "-----BEGIN ELGAMAL PUBLIC KEY-----":
        raise ValueError("Invalid public key format")
    p = int.from_bytes(b64decode(lines[1]))
    g = int.from_bytes(b64decode(lines[2]))
    y = int.from_bytes(b64decode(lines[3]))
    return p, g, y


def _import_priv(pem: str):
    lines = pem.strip().splitlines()
    if lines[0] != "-----BEGIN ELGAMAL PRIVATE KEY-----":
        raise ValueError("Invalid private key format")
    p = int.from_bytes(b64decode(lines[1]))
    g = int.from_bytes(b64decode(lines[2]))
    y = int.from_bytes(b64decode(lines[3]))
    x = int.from_bytes(b64decode(lines[4]))
    return p, g, y, x


def encrypt(pub_pem: str, plaintext: str) -> bytes:
    p, g, y = _import_pub(pub_pem)
    bl = (p.bit_length() + 7) // 8
    k = int.from_bytes(get_random_bytes(bl)) % (p - 1)
    if k == 0:
        k = 1
    c1 = pow(g, k, p)
    s = pow(y, k, p)
    shared = SHA256.new(s.to_bytes(bl)).digest()[:16]
    nonce = get_random_bytes(12)
    cipher = AES.new(shared, AES.MODE_GCM, nonce=nonce)
    ct, tag = cipher.encrypt_and_digest(plaintext.encode())
    return c1.to_bytes(bl) + nonce + tag + ct


def decrypt(priv_pem: str, data: bytes) -> str:
    p, g, y, x = _import_priv(priv_pem)
    bl = (p.bit_length() + 7) // 8
    c1 = int.from_bytes(data[:bl])
    nonce = data[bl : bl + 12]
    tag = data[bl + 12 : bl + 28]
    ct = data[bl + 28 :]
    s = pow(c1, x, p)
    shared = SHA256.new(s.to_bytes(bl)).digest()[:16]
    cipher = AES.new(shared, AES.MODE_GCM, nonce=nonce)
    return cipher.decrypt_and_verify(ct, tag).decode()
