from ...base.encoder import Encoder
from ..fun.bits import bits_chunk_encode, bits_chunk_decode

_CHINESE = [chr(0x4EBA + i) for i in range(256)]


class ChineseEncoder(Encoder):
    name = "Chinese"

    def encode(self, data: bytes) -> str:
        return bits_chunk_encode(data, _CHINESE, 8)

    def decode(self, text: str) -> bytes:
        return bits_chunk_decode(text, _CHINESE, 8)
