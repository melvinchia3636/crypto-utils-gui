from ...base.encoder import Encoder

from .bits import bits_chunk_encode, bits_chunk_decode

_CIRCLEDPAREN = [chr(0x2474 + i) for i in range(16)]


class CircledParenEncoder(Encoder):
    name = "Circled Paren"

    def encode(self, data: bytes) -> str:
        return bits_chunk_encode(data, _CIRCLEDPAREN, 4)

    def decode(self, text: str) -> bytes:
        return bits_chunk_decode(text, _CIRCLEDPAREN, 4)
