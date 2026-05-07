from base64 import a85decode, a85encode

from ...base.encoder import Encoder


class Base85Encoder(Encoder):
    name = "Base85"

    def encode(self, data: bytes) -> str:
        return a85encode(data).decode()

    def decode(self, text: str) -> bytes:
        return a85decode(text.encode())
