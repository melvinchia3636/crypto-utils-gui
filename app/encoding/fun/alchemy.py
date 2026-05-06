from ...base.encoder import Encoder
from .bars import _bits_chunk_encode, _bits_chunk_decode

_ALCHEMY = ["☿", "♄", "♃", "♆", "♇", "🜁", "🜂", "🜃"]


class AlchemyEncoder(Encoder):
    name = "Alchemy"

    def encode(self, data: bytes) -> str:
        return _bits_chunk_encode(data, _ALCHEMY, 3)

    def decode(self, text: str) -> bytes:
        return _bits_chunk_decode(text, _ALCHEMY, 3)
