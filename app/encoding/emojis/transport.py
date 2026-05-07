from ...base.encoder import Encoder
from ..fun.bits import bits_chunk_encode, bits_chunk_decode

_TRANSPORT = [
    "🚗",
    "🚕",
    "🚙",
    "🚌",
    "🚎",
    "🏎",
    "🚓",
    "🚑",
    "🚒",
    "🚐",
    "🚚",
    "🚛",
    "🚜",
    "🚲",
    "🛵",
    "🚁",
]


class TransportEncoder(Encoder):
    name = "Transport"

    def encode(self, data: bytes) -> str:
        return bits_chunk_encode(data, _TRANSPORT, 4)

    def decode(self, text: str) -> bytes:
        return bits_chunk_decode(text, _TRANSPORT, 4)
