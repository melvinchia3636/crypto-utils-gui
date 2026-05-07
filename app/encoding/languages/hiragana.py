import unicodedata
from ...base.encoder import Encoder

from ..fun.bits import bits_chunk_encode, bits_chunk_decode

_HIRAGANA = [chr(cp) for cp in range(0x3040, 0x30A0) if unicodedata.name(chr(cp), "")][
    :64
]


class HiraganaEncoder(Encoder):
    name = "Hiragana"

    def encode(self, data: bytes) -> str:
        return bits_chunk_encode(data, _HIRAGANA, 6)

    def decode(self, text: str) -> bytes:
        return bits_chunk_decode(text, _HIRAGANA, 6)
