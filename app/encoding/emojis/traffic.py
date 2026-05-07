from ...base.encoder import Encoder
from ..fun.bits import bits_chunk_encode, bits_chunk_decode

_TRAFFIC = ["\U0001f6a6", "\U0001f6a5"]


class TrafficEncoder(Encoder):
    name = "Traffic"

    def encode(self, data: bytes) -> str:
        return bits_chunk_encode(data, _TRAFFIC, 1)

    def decode(self, text: str) -> bytes:
        return bits_chunk_decode(text, _TRAFFIC, 1)
