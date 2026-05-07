import unicodedata
from ...base.encoder import Encoder

from .bits import bits_chunk_encode, bits_chunk_decode

_DOUBLESTRUCK = []
for cp in range(0x1D538, 0x1D56C):
    c = chr(cp)
    if len(c) == 1 and unicodedata.name(c, ""):
        _DOUBLESTRUCK.append(c)
        if len(_DOUBLESTRUCK) >= 32:
            break


class DoublestruckEncoder(Encoder):
    name = "Double-struck"

    def encode(self, data: bytes) -> str:
        return bits_chunk_encode(data, _DOUBLESTRUCK, 5)

    def decode(self, text: str) -> bytes:
        return bits_chunk_decode(text, _DOUBLESTRUCK, 5)
