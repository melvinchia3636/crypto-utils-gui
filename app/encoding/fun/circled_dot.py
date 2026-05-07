from ...base.encoder import Encoder

from .bits import bits_chunk_encode, bits_chunk_decode

_CIRCLEDDOT = [chr(0x2488 + i) for i in range(16)]


class CircledDotEncoder(Encoder):
    name = "Circled Dot"

    def encode(self, data: bytes) -> str:
        return bits_chunk_encode(data, _CIRCLEDDOT, 4)

    def decode(self, text: str) -> bytes:
        return bits_chunk_decode(text, _CIRCLEDDOT, 4)
