from ...base.encoder import Encoder

from .bits import bits_chunk_encode, bits_chunk_decode

_ROMAN_LOW = [
    "ⅰ",
    "ⅱ",
    "ⅲ",
    "ⅳ",
    "ⅴ",
    "ⅵ",
    "ⅶ",
    "ⅷ",
    "ⅸ",
    "ⅹ",
    "ⅺ",
    "ⅻ",
    "ⅼ",
    "ⅽ",
    "ⅾ",
    "ⅿ",
]


class RomanLowEncoder(Encoder):
    name = "Roman Low"

    def encode(self, data: bytes) -> str:
        return bits_chunk_encode(data, _ROMAN_LOW, 4)

    def decode(self, text: str) -> bytes:
        return bits_chunk_decode(text, _ROMAN_LOW, 4)
