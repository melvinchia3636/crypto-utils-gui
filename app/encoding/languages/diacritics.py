import unicodedata
from ...base.encoder import Encoder
from ..fun.bits import bits_chunk_encode, bits_chunk_decode

_DIACRITICS = []
for cp in range(0x0300, 0x0370):
    c = chr(cp)
    if len(c) == 1 and unicodedata.name(c, ''):
        _DIACRITICS.append(c)
        if len(_DIACRITICS) >= 64:
            break


class DiacriticsEncoder(Encoder):
    name = "Diacritics"

    def encode(self, data: bytes) -> str:
        return bits_chunk_encode(data, _DIACRITICS, 6)

    def decode(self, text: str) -> bytes:
        return bits_chunk_decode(text, _DIACRITICS, 6)
