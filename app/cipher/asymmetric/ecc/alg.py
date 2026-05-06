from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto.PublicKey import ECC
from Crypto.Random import get_random_bytes
from Crypto.Signature import DSS

_CURVE_BYTES = {"NIST P-256": 32, "NIST P-384": 48, "NIST P-521": 66}
_CURVE_MAP = {"P-256": "NIST P-256", "P-384": "NIST P-384", "P-521": "NIST P-521"}


def generate_keypair(curve: str = "P-256") -> tuple[str, str]:
    key = ECC.generate(curve=_CURVE_MAP[curve])
    pub = key.public_key().export_key(format="PEM")
    priv = key.export_key(format="PEM")
    return pub, priv


def encrypt(pub_pem: str, plaintext: str) -> bytes:
    pubkey = ECC.import_key(pub_pem)
    eph_key = ECC.generate(curve=pubkey.curve)
    shared_point = eph_key.d * pubkey.pointQ
    shared_secret = SHA256.new(shared_point.x.to_bytes(_CURVE_BYTES[pubkey.curve]))
    aes_key = shared_secret.digest()[:16]
    nonce = get_random_bytes(12)
    cipher = AES.new(aes_key, AES.MODE_GCM, nonce=nonce)
    ct, tag = cipher.encrypt_and_digest(plaintext.encode())
    eph_pub = eph_key.public_key().export_key(format="PEM")
    result = eph_pub.encode() + b"\n---ECCSEP---\n" + nonce + tag + ct
    return result


def decrypt(priv_pem: str, data: bytes) -> str:
    seph = b"\n---ECCSEP---\n"
    idx = data.index(seph)
    eph_pem = data[:idx].decode()
    rest = data[idx + len(seph) :]
    nonce = rest[:12]
    tag = rest[12:28]
    ct = rest[28:]
    privkey = ECC.import_key(priv_pem)
    eph_pubkey = ECC.import_key(eph_pem)
    shared_point = privkey.d * eph_pubkey.pointQ
    shared_secret = SHA256.new(shared_point.x.to_bytes(_CURVE_BYTES[privkey.curve]))
    aes_key = shared_secret.digest()[:16]
    cipher = AES.new(aes_key, AES.MODE_GCM, nonce=nonce)
    return cipher.decrypt_and_verify(ct, tag).decode()


def sign(priv_pem: str, message: str) -> bytes:
    privkey = ECC.import_key(priv_pem)
    h = SHA256.new(message.encode())
    signer = DSS.new(privkey, "fips-186-3")
    return signer.sign(h)


def verify(pub_pem: str, message: str, signature: bytes) -> bool:
    pubkey = ECC.import_key(pub_pem)
    h = SHA256.new(message.encode())
    verifier = DSS.new(pubkey, "fips-186-3")
    try:
        verifier.verify(h, signature)
        return True
    except ValueError:
        return False
