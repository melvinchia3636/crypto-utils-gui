from ...base.encoder import Encoder

from .bits import bits_chunk_encode, bits_chunk_decode

_CIRCLED = [chr(0x2460 + i) for i in range(16)]


class CircledEncoder(Encoder):
    name = "Circled"

    def encode(self, data: bytes) -> str:
        return bits_chunk_encode(data, _CIRCLED, 4)

    def decode(self, text: str) -> bytes:
        return bits_chunk_decode(text, _CIRCLED, 4)
