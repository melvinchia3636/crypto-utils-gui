from ...base.encoder import Encoder
from base64 import b32encode, b32decode


class Base32Encoder(Encoder):
    name = "Base32"

    def encode(self, data: bytes) -> str:
        return b32encode(data).decode()

    def decode(self, text: str) -> bytes:
        return b32decode(text.encode())
