from ...base.encoder import Encoder

from .bits import bits_chunk_encode, bits_chunk_decode

_ROMAN_CAP = [
    "Ⅰ",
    "Ⅱ",
    "Ⅲ",
    "Ⅳ",
    "Ⅴ",
    "Ⅵ",
    "Ⅶ",
    "Ⅷ",
    "Ⅸ",
    "Ⅹ",
    "Ⅺ",
    "Ⅻ",
    "Ⅼ",
    "Ⅽ",
    "Ⅾ",
    "Ⅿ",
]


class RomanCapEncoder(Encoder):
    name = "Roman Cap"

    def encode(self, data: bytes) -> str:
        return bits_chunk_encode(data, _ROMAN_CAP, 4)

    def decode(self, text: str) -> bytes:
        return bits_chunk_decode(text, _ROMAN_CAP, 4)
