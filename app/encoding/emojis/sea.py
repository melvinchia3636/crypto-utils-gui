from ...base.encoder import Encoder
from ..fun.bits import bits_chunk_encode, bits_chunk_decode

_SEA = ["🐟", "🐠", "🐡", "🦈", "🐙", "🦑", "🦐", "🦞", "🦀", "🐳", "🐋", "🐬", "🐚", "🪸", "🐊", "🦭"]


class SeaEncoder(Encoder):
    name = "Sea Life"

    def encode(self, data: bytes) -> str:
        return bits_chunk_encode(data, _SEA, 4)

    def decode(self, text: str) -> bytes:
        return bits_chunk_decode(text, _SEA, 4)
