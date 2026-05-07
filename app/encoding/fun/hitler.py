from ...base.encoder import Encoder
from .bits import bits_chunk_encode, bits_chunk_decode

_HITLER = ["卐", "卍"]


class HitlerEncoder(Encoder):
    name = "Hitler"

    def encode(self, data: bytes) -> str:
        return bits_chunk_encode(data, _HITLER, 1)

    def decode(self, text: str) -> bytes:
        return bits_chunk_decode(text, _HITLER, 1)
