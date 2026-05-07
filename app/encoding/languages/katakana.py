import unicodedata
from ...base.encoder import Encoder

from ..fun.bits import bits_chunk_encode, bits_chunk_decode

_KATAKANA = [chr(cp) for cp in range(0x30A0, 0x3100) if unicodedata.name(chr(cp), "")][
    :64
]


class KatakanaEncoder(Encoder):
    name = "Katakana"

    def encode(self, data: bytes) -> str:
        return bits_chunk_encode(data, _KATAKANA, 6)

    def decode(self, text: str) -> bytes:
        return bits_chunk_decode(text, _KATAKANA, 6)
