from ...base.encoder import Encoder
from base64 import b64encode, b64decode


class HexEncoder(Encoder):
    name = "Hex"

    def encode(self, data: bytes) -> str:
        return data.hex()

    def decode(self, text: str) -> bytes:
        return bytes.fromhex(text)
