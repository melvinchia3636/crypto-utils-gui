from ...base.encoder import Encoder
from .bits import bits_chunk_encode, bits_chunk_decode

_STARS = [
    "★",
    "☆",
    "✡",
    "✢",
    "✣",
    "✤",
    "✥",
    "✦",
]


class StarsEncoder(Encoder):
    name = "Stars"

    def encode(self, data: bytes) -> str:
        return bits_chunk_encode(data, _STARS, 3)

    def decode(self, text: str) -> bytes:
        return bits_chunk_decode(text, _STARS, 3)
