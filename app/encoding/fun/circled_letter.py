from ...base.encoder import Encoder

from .bits import bits_chunk_encode, bits_chunk_decode

_CIRCLEDLETTER = [chr(0x24B6 + i) for i in range(16)]


class CircledLetterEncoder(Encoder):
    name = "Circled Letter"

    def encode(self, data: bytes) -> str:
        return bits_chunk_encode(data, _CIRCLEDLETTER, 4)

    def decode(self, text: str) -> bytes:
        return bits_chunk_decode(text, _CIRCLEDLETTER, 4)
