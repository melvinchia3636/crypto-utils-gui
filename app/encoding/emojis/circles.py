from ...base.encoder import Encoder
from ..fun.bits import bits_chunk_encode, bits_chunk_decode

_CIRCLES = [
    "\U0001f534",
    "\U0001f7e0",
    "\U0001f7e1",
    "\U0001f7e2",
    "\U0001f535",
    "\U0001f7e3",
    "\U0001f7e4",
    "\U0001f518",
]


class CirclesEncoder(Encoder):
    name = "Circles"

    def encode(self, data: bytes) -> str:
        return bits_chunk_encode(data, _CIRCLES, 3)

    def decode(self, text: str) -> bytes:
        return bits_chunk_decode(text, _CIRCLES, 3)
