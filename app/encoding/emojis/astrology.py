from ...base.encoder import Encoder
from ..fun.bits import bits_chunk_encode, bits_chunk_decode

_ASTROLOGY = ["♈", "♉", "♊", "♋", "♌", "♍", "♎", "♏"]


class AstrologyEncoder(Encoder):
    name = "Astrology"

    def encode(self, data: bytes) -> str:
        return bits_chunk_encode(data, _ASTROLOGY, 3)

    def decode(self, text: str) -> bytes:
        return bits_chunk_decode(text, _ASTROLOGY, 3)
