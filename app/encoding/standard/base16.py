from base64 import b16decode, b16encode

from ...base.encoder import Encoder


class Base16Encoder(Encoder):
    name = "Base16"

    def encode(self, data: bytes) -> str:
        return b16encode(data).decode()

    def decode(self, text: str) -> bytes:
        return b16decode(text.encode())
