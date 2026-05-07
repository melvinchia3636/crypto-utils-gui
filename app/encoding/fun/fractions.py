from ...base.encoder import Encoder

from .bits import bits_chunk_encode, bits_chunk_decode

_FRACTIONS = [
    "⅓",
    "⅔",
    "⅕",
    "⅖",
    "⅗",
    "⅘",
    "⅙",
    "⅚",
    "⅛",
    "⅜",
    "⅝",
    "⅞",
    "⅟",
    "½",
    "¼",
    "¾",
]


class FractionsEncoder(Encoder):
    name = "Fractions"

    def encode(self, data: bytes) -> str:
        return bits_chunk_encode(data, _FRACTIONS, 4)

    def decode(self, text: str) -> bytes:
        return bits_chunk_decode(text, _FRACTIONS, 4)
