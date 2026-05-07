from ...base.encoder import Encoder
from ..fun.bits import bits_chunk_encode, bits_chunk_decode

_HIEROGLYPHS = [chr(0x13000 + i) for i in range(256)]


class HieroglyphEncoder(Encoder):
    name = "Hieroglyph"

    def encode(self, data: bytes) -> str:
        return bits_chunk_encode(data, _HIEROGLYPHS, 8)

    def decode(self, text: str) -> bytes:
        return bits_chunk_decode(text, _HIEROGLYPHS, 8)
