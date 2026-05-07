from ...base.encoder import Encoder

from .bits import bits_chunk_encode, bits_chunk_decode

_ASCII = "".join(chr(i) for i in range(33, 127))
_EXTRA = "".join(chr(i) for i in range(192, 256))
_BASE128 = _ASCII + _EXTRA


class Base128Encoder(Encoder):
    name = "Base128"

    def encode(self, data: bytes) -> str:
        return bits_chunk_encode(data, _BASE128, 7)

    def decode(self, text: str) -> bytes:
        return bits_chunk_decode(text, _BASE128, 7)
