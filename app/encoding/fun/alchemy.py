from ...base.encoder import Encoder
from .bits import bits_chunk_decode, bits_chunk_encode

_ALCHEMY = ["☿", "♄", "♃", "♆", "♇", "🜁", "🜂", "🜃"]


class AlchemyEncoder(Encoder):
    name = "Alchemy"

    def encode(self, data: bytes) -> str:
        return bits_chunk_encode(data, _ALCHEMY, 3)

    def decode(self, text: str) -> bytes:
        return bits_chunk_decode(text, _ALCHEMY, 3)
