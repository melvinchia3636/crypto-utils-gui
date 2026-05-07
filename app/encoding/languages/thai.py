import unicodedata
from ...base.encoder import Encoder

_THAI = []
for cp in range(0x0E00, 0x0E80):
    c = chr(cp)
    if len(c) == 1 and unicodedata.name(c, ""):
        _THAI.append(c)
        if len(_THAI) >= 64:
            break

from ..fun.bits import bits_chunk_encode, bits_chunk_decode


class ThaiEncoder(Encoder):
    name = "Thai"

    def encode(self, data: bytes) -> str:
        return bits_chunk_encode(data, _THAI, 6)

    def decode(self, text: str) -> bytes:
        return bits_chunk_decode(text, _THAI, 6)
