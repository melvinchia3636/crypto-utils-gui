from ...base.encoder import Encoder
from ..fun.bits import bits_chunk_encode, bits_chunk_decode

_FOOD = [
    "🍎",
    "🍏",
    "🍐",
    "🍑",
    "🍒",
    "🍓",
    "🍅",
    "🍆",
    "🍇",
    "🍈",
    "🍉",
    "🍊",
    "🍋",
    "🍌",
    "🍍",
    "🌽",
]


class FoodEncoder(Encoder):
    name = "Food"

    def encode(self, data: bytes) -> str:
        return bits_chunk_encode(data, _FOOD, 4)

    def decode(self, text: str) -> bytes:
        return bits_chunk_decode(text, _FOOD, 4)
