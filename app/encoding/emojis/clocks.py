from ...base.encoder import Encoder
from ..fun.bits import bits_chunk_encode, bits_chunk_decode

_CLOCKS = [
    "🕐",
    "🕑",
    "🕒",
    "🕓",
    "🕔",
    "🕕",
    "🕖",
    "🕗",
    "🕘",
    "🕙",
    "🕚",
    "🕛",
    "🕜",
    "🕝",
    "🕞",
    "🕟",
]


class ClocksEncoder(Encoder):
    name = "Clocks"

    def encode(self, data: bytes) -> str:
        return bits_chunk_encode(data, _CLOCKS, 4)

    def decode(self, text: str) -> bytes:
        return bits_chunk_decode(text, _CLOCKS, 4)
