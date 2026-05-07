from ...base.encoder import Encoder
from ..fun.bits import bits_chunk_encode, bits_chunk_decode

_ANIMALS = [
    "🐶",
    "🐱",
    "🐭",
    "🐹",
    "🐰",
    "🦊",
    "🐻",
    "🐼",
    "🐨",
    "🐯",
    "🦁",
    "🐮",
    "🐷",
    "🐸",
    "🐵",
    "🐔",
]


class AnimalsEncoder(Encoder):
    name = "Animals"

    def encode(self, data: bytes) -> str:
        return bits_chunk_encode(data, _ANIMALS, 4)

    def decode(self, text: str) -> bytes:
        return bits_chunk_decode(text, _ANIMALS, 4)
