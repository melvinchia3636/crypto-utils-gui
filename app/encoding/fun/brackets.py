from ...base.encoder import Encoder
from ..fun.bits import bits_chunk_encode, bits_chunk_decode

_BRACKETS = ["(", ")", "[", "]", "{", "}", "<", ">"]


class BracketsEncoder(Encoder):
    name = "Brackets"

    def encode(self, data: bytes) -> str:
        return bits_chunk_encode(data, _BRACKETS, 3)

    def decode(self, text: str) -> bytes:
        return bits_chunk_decode(text, _BRACKETS, 3)
