from ...base.encoder import Encoder
from .bits import bits_chunk_encode, bits_chunk_decode

_COMPASS = ["N", "E", "S", "W"]


class CompassEncoder(Encoder):
    name = "Compass"

    def encode(self, data: bytes) -> str:
        return bits_chunk_encode(data, _COMPASS, 2)

    def decode(self, text: str) -> bytes:
        return bits_chunk_decode(text, _COMPASS, 2)
