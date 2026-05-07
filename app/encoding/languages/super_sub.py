import unicodedata
from ...base.encoder import Encoder
from ..fun.bits import bits_chunk_encode, bits_chunk_decode

_SCRIPT = []
for cp in range(0x2070, 0x20A0):
    c = chr(cp)
    if len(c) == 1 and unicodedata.name(c, ''):
        _SCRIPT.append(c)

_SCRIPT = _SCRIPT[:32]


class SuperSubEncoder(Encoder):
    name = "Super/Sub"

    def encode(self, data: bytes) -> str:
        return bits_chunk_encode(data, _SCRIPT, 5)

    def decode(self, text: str) -> bytes:
        return bits_chunk_decode(text, _SCRIPT, 5)
