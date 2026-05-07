import unicodedata
from ...base.encoder import Encoder
from ..fun.bits import bits_chunk_encode, bits_chunk_decode

_TAMIL = []
for cp in range(0x0B80, 0x0C00):
    c = chr(cp)
    if len(c) == 1 and unicodedata.name(c, ""):
        name = unicodedata.name(c, "").upper()
        if "VOWEL SIGN" in name or "VIRAMA" in name or "SIGN" in name:
            continue
        _TAMIL.append(c)
        if len(_TAMIL) >= 32:
            break


class TamilEncoder(Encoder):
    name = "Tamil"

    def encode(self, data: bytes) -> str:
        return bits_chunk_encode(data, _TAMIL, 5)

    def decode(self, text: str) -> bytes:
        return bits_chunk_decode(text, _TAMIL, 5)
