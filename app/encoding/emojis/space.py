from ...base.encoder import Encoder
from ..fun.bits import bits_chunk_encode, bits_chunk_decode

_SPACE = [
    "☀",
    "🌙",
    "⭐",
    "🌟",
    "🌚",
    "🌛",
    "🌜",
    "🌝",
    "🌞",
    "🪐",
    "🌍",
    "🌎",
    "🌏",
    "🌑",
    "🌒",
    "🌓",
]


class SpaceEncoder(Encoder):
    name = "Space"

    def encode(self, data: bytes) -> str:
        return bits_chunk_encode(data, _SPACE, 4)

    def decode(self, text: str) -> bytes:
        return bits_chunk_decode(text, _SPACE, 4)
