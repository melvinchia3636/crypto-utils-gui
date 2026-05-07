import unicodedata
from ...base.encoder import Encoder
from ..fun.bits import bits_chunk_encode, bits_chunk_decode

_IPA = []
for cp in range(0x0250, 0x02D0):
    c = chr(cp)
    if len(c) == 1 and unicodedata.name(c, ""):
        _IPA.append(c)
        if len(_IPA) >= 128:
            break


class IpaEncoder(Encoder):
    name = "IPA"

    def encode(self, data: bytes) -> str:
        return bits_chunk_encode(data, _IPA, 7)

    def decode(self, text: str) -> bytes:
        return bits_chunk_decode(text, _IPA, 7)
