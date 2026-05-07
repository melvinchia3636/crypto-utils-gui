from ...base.encoder import Encoder
from ..fun.bits import bits_chunk_encode, bits_chunk_decode

_KOREAN = [chr(0xAC00 + i) for i in range(256)]


class KoreanEncoder(Encoder):
    name = "Korean"

    def encode(self, data: bytes) -> str:
        return bits_chunk_encode(data, _KOREAN, 8)

    def decode(self, text: str) -> bytes:
        return bits_chunk_decode(text, _KOREAN, 8)
