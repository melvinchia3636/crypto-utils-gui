from ...base.encoder import Encoder
from ..fun.bits import bits_chunk_encode, bits_chunk_decode

_GEARS = ["\u2699", "\U0001F527", "\U0001F528", "\U0001F529", "\u26A1", "\U0001F50C", "\U0001F50B", "\U0001F4BB"]


class GearsEncoder(Encoder):
    name = "Gears"

    def encode(self, data: bytes) -> str:
        return bits_chunk_encode(data, _GEARS, 3)

    def decode(self, text: str) -> bytes:
        return bits_chunk_decode(text, _GEARS, 3)
