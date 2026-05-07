from ...base.encoder import Encoder
from ..fun.bits import bits_chunk_encode, bits_chunk_decode

_SPORTS = ["⚽", "🏀", "🏈", "⚾", "🎾", "🏐", "🏉", "🎱", "🏓", "🏸", "🏒", "🏑", "🏏", "🥊", "🥋", "⛸"]


class SportsEncoder(Encoder):
    name = "Sports"

    def encode(self, data: bytes) -> str:
        return bits_chunk_encode(data, _SPORTS, 4)

    def decode(self, text: str) -> bytes:
        return bits_chunk_decode(text, _SPORTS, 4)
