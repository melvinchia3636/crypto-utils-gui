from ...base.encoder import Encoder
from .bars import _bits_chunk_decode, _bits_chunk_encode

_RUNES = "ᚠᚢᚦᚨᚱᚲᚷᚹᚺᚾᛁᛃᛇᛉᛊᛋ"


class RunesEncoder(Encoder):
    name = "Runes"

    def encode(self, data: bytes) -> str:
        return _bits_chunk_encode(data, _RUNES, 4)

    def decode(self, text: str) -> bytes:
        return _bits_chunk_decode(text, _RUNES, 4)
