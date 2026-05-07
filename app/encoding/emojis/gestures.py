from ...base.encoder import Encoder
from ..fun.bits import bits_chunk_encode, bits_chunk_decode

_GESTURES = [
    "\U0001F44B", "\U0001F91A", "\U0001F590", "\u270B", "\U0001F596", "\U0001FAF1", "\U0001FAF2",
    "\U0001F44C", "\u270C", "\U0001F91F", "\U0001F919", "\U0001F91E", "\U0001F44D", "\U0001F44E",
    "\u270A", "\U0001F44A", "\U0001F91B", "\U0001F91C", "\U0001F44F", "\U0001F64C", "\U0001FAF6",
    "\U0001F450", "\U0001F91D", "\U0001F64F",
]


class GesturesEncoder(Encoder):
    name = "Gestures"

    def encode(self, data: bytes) -> str:
        return bits_chunk_encode(data, _GESTURES[:16], 4)

    def decode(self, text: str) -> bytes:
        return bits_chunk_decode(text, _GESTURES[:16], 4)
