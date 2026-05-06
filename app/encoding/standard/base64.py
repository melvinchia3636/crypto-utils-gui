from ..encoder import Encoder
from base64 import b64encode, b64decode


class Base64Encoder(Encoder):
    name = "Base64"

    def encode(self, data: bytes) -> str:
        return b64encode(data).decode()

    def decode(self, text: str) -> bytes:
        return b64decode(text.encode())
