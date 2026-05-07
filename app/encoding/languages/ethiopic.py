import unicodedata
from ...base.encoder import Encoder
from ..fun.bits import bits_chunk_encode, bits_chunk_decode

_ETHIOPIC = []
for cp in range(0x1200, 0x1380):
    c = chr(cp)
    if len(c) == 1 and unicodedata.name(c, ''):
        _ETHIOPIC.append(c)
        if len(_ETHIOPIC) >= 256:
            break


class EthiopicEncoder(Encoder):
    name = "Ethiopic"

    def encode(self, data: bytes) -> str:
        return bits_chunk_encode(data, _ETHIOPIC, 8)

    def decode(self, text: str) -> bytes:
        return bits_chunk_decode(text, _ETHIOPIC, 8)
