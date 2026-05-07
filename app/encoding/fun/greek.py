import unicodedata
from ...base.encoder import Encoder

from .bits import bits_chunk_encode, bits_chunk_decode

_GREEK = []
for cp in range(0x0391, 0x03AA):
    c = chr(cp)
    if len(c) == 1 and unicodedata.name(c, ""):
        _GREEK.append(c)
for cp in range(0x03B1, 0x03CA):
    c = chr(cp)
    if len(c) == 1 and unicodedata.name(c, ""):
        _GREEK.append(c)

_GREEK = _GREEK[:32]


class GreekEncoder(Encoder):
    name = "Greek"

    def encode(self, data: bytes) -> str:
        return bits_chunk_encode(data, _GREEK, 5)

    def decode(self, text: str) -> bytes:
        return bits_chunk_decode(text, _GREEK, 5)
