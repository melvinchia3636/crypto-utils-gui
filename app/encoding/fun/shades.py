from ...base.encoder import Encoder
from .bits import bits_chunk_encode, bits_chunk_decode

_SHADES = ["░", "▒", "▓", "█"]


class ShadesEncoder(Encoder):
    name = "Shades"

    def encode(self, data: bytes) -> str:
        return bits_chunk_encode(data, _SHADES, 2)

    def decode(self, text: str) -> bytes:
        return bits_chunk_decode(text, _SHADES, 2)
