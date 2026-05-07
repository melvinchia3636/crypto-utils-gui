import unicodedata
from ...base.encoder import Encoder
from ..fun.bits import bits_chunk_encode, bits_chunk_decode

_GLAG = []
for cp in range(0x2C00, 0x2C60):
    c = chr(cp)
    if len(c) == 1 and unicodedata.name(c, ''):
        _GLAG.append(c)
        if len(_GLAG) >= 64:
            break


class GlagoliticEncoder(Encoder):
    name = "Glagolitic"

    def encode(self, data: bytes) -> str:
        return bits_chunk_encode(data, _GLAG, 6)

    def decode(self, text: str) -> bytes:
        return bits_chunk_decode(text, _GLAG, 6)
