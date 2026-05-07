import unicodedata
from ...base.encoder import Encoder

from ..fun.bits import bits_chunk_encode, bits_chunk_decode

_DUPLOYAN = []
for cp in range(0x1BC00, 0x1BD00):
    c = chr(cp)
    if len(c) == 1 and unicodedata.name(c, ""):
        _DUPLOYAN.append(c)
        if len(_DUPLOYAN) >= 128:
            break


class DuployanEncoder(Encoder):
    name = "Duployan"

    def encode(self, data: bytes) -> str:
        return bits_chunk_encode(data, _DUPLOYAN, 7)

    def decode(self, text: str) -> bytes:
        return bits_chunk_decode(text, _DUPLOYAN, 7)
