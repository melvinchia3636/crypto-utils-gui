from ...base.encoder import Encoder

from .bits import bits_chunk_encode, bits_chunk_decode

_DOUBLECIRCLED = [chr(0x24F5 + i) for i in range(8)]


class DoubleCircledEncoder(Encoder):
    name = "Double Circled"

    def encode(self, data: bytes) -> str:
        return bits_chunk_encode(data, _DOUBLECIRCLED, 3)

    def decode(self, text: str) -> bytes:
        return bits_chunk_decode(text, _DOUBLECIRCLED, 3)
