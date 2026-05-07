import unicodedata
from ...base.encoder import Encoder
from .bits import bits_chunk_encode, bits_chunk_decode

_SCRIPT = []
for cp in range(0x1D49C, 0x1D4D0):
    c = chr(cp)
    if len(c) == 1 and unicodedata.name(c, ""):
        _SCRIPT.append(c)
        if len(_SCRIPT) >= 32:
            break


class ScriptEncoder(Encoder):
    name = "Script"

    def encode(self, data: bytes) -> str:
        return bits_chunk_encode(data, _SCRIPT, 5)

    def decode(self, text: str) -> bytes:
        return bits_chunk_decode(text, _SCRIPT, 5)
