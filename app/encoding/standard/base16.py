from ...base.encoder import Encoder
from base64 import b16encode, b16decode


class Base16Encoder(Encoder):
    name = "Base16"

    def encode(self, data: bytes) -> str:
        return b16encode(data).decode()

    def decode(self, text: str) -> bytes:
        return b16decode(text.encode())
