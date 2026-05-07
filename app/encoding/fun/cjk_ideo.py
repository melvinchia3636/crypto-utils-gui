from ...base.encoder import Encoder

from .bits import bits_chunk_encode, bits_chunk_decode

_CJKIDEO = [chr(0x3358 + i) for i in range(16)]


class CjkIdeoEncoder(Encoder):
    name = "CJK Ideo"

    def encode(self, data: bytes) -> str:
        return bits_chunk_encode(data, _CJKIDEO, 4)

    def decode(self, text: str) -> bytes:
        return bits_chunk_decode(text, _CJKIDEO, 4)
