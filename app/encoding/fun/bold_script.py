import unicodedata
from ...base.encoder import Encoder

from .bits import bits_chunk_encode, bits_chunk_decode

_BOLDSCRIPT = []
for cp in range(0x1D4D0, 0x1D504):
    c = chr(cp)
    if len(c) == 1 and unicodedata.name(c, ""):
        _BOLDSCRIPT.append(c)
        if len(_BOLDSCRIPT) >= 32:
            break


class BoldScriptEncoder(Encoder):
    name = "Bold Script"

    def encode(self, data: bytes) -> str:
        return bits_chunk_encode(data, _BOLDSCRIPT, 5)

    def decode(self, text: str) -> bytes:
        return bits_chunk_decode(text, _BOLDSCRIPT, 5)
