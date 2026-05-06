
from ...base.encoder import Encoder


class HexEncoder(Encoder):
    name = "Hex"

    def encode(self, data: bytes) -> str:
        return data.hex()

    def decode(self, text: str) -> bytes:
        return bytes.fromhex(text)
