from ...base.encoder import Encoder
from .bits import bits_chunk_encode, bits_chunk_decode

_BARS = ["▁", "▂", "▃", "▄", "▅", "▆", "▇", "█"]


class BarsEncoder(Encoder):
    name = "Bars"

    def encode(self, data: bytes) -> str:
        return bits_chunk_encode(data, _BARS, 3)

    def decode(self, text: str) -> bytes:
        return bits_chunk_decode(text, _BARS, 3)
