from ...base.encoder import Encoder
from .bits import bits_chunk_encode, bits_chunk_decode

_BF = ["+", "-", "<", ">", "[", "]", ".", ","]


class BrainfuckEncoder(Encoder):
    name = "Brainfuck"

    def encode(self, data: bytes) -> str:
        return bits_chunk_encode(data, _BF, 3)

    def decode(self, text: str) -> bytes:
        return bits_chunk_decode(text, _BF, 3)
