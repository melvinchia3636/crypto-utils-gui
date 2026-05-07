from ...base.encoder import Encoder
from ..fun.bits import bits_chunk_encode, bits_chunk_decode

_INSTRUMENTS = [
    "🎹",
    "🎸",
    "🎻",
    "🎷",
    "🎺",
    "🥁",
    "🎵",
    "🎶",
]


class InstrumentsEncoder(Encoder):
    name = "Instruments"

    def encode(self, data: bytes) -> str:
        return bits_chunk_encode(data, _INSTRUMENTS, 3)

    def decode(self, text: str) -> bytes:
        return bits_chunk_decode(text, _INSTRUMENTS, 3)
