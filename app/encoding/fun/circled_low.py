from ...base.encoder import Encoder

from .bits import bits_chunk_encode, bits_chunk_decode

_CIRCLEDLOW = [chr(0x24D0 + i) for i in range(16)]


class CircledLowEncoder(Encoder):
    name = "Circled Low"

    def encode(self, data: bytes) -> str:
        return bits_chunk_encode(data, _CIRCLEDLOW, 4)

    def decode(self, text: str) -> bytes:
        return bits_chunk_decode(text, _CIRCLEDLOW, 4)
