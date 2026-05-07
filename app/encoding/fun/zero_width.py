from ...base.encoder import Encoder
from .bits import bits_chunk_encode, bits_chunk_decode

_ZW = ["\u200D", "\u200C", "\u200B", "\uFEFF"]


class ZeroWidthEncoder(Encoder):
    name = "Zero Width"

    def encode(self, data: bytes) -> str:
        encoded = bits_chunk_encode(data, _ZW, 2)
        return "\u2588".join(encoded)

    def decode(self, text: str) -> bytes:
        cleaned = text.replace("\u2588", "")
        return bits_chunk_decode(cleaned, _ZW, 2)
