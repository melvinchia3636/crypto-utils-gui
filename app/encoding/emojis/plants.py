from ...base.encoder import Encoder
from ..fun.bits import bits_chunk_encode, bits_chunk_decode

_PLANTS = [
    "🌱",
    "🌿",
    "☘",
    "🍀",
    "🌺",
    "🌸",
    "🌼",
    "🌻",
    "🌷",
    "🌹",
    "🥀",
    "🌾",
    "🌵",
    "🎄",
    "🌲",
    "🌳",
]


class PlantsEncoder(Encoder):
    name = "Plants"

    def encode(self, data: bytes) -> str:
        return bits_chunk_encode(data, _PLANTS, 4)

    def decode(self, text: str) -> bytes:
        return bits_chunk_decode(text, _PLANTS, 4)
