from ...base.encoder import Encoder
from .bits import bits_chunk_encode, bits_chunk_decode

_SHAPES = [
    "\u25A0", "\u25A1", "\u25A2", "\u25A3", "\u25A4", "\u25A5", "\u25A6", "\u25A7",
    "\u25A8", "\u25A9", "\u25AA", "\u25AB", "\u25AC", "\u25AD", "\u25AE", "\u25AF",
    "\u25B0", "\u25B1", "\u25B2", "\u25B3", "\u25B4", "\u25B5", "\u25B6", "\u25B7",
    "\u25B8", "\u25B9", "\u25BA", "\u25BB", "\u25BC", "\u25BD", "\u25BE", "\u25BF",
    "\u25C0", "\u25C1", "\u25C2", "\u25C3", "\u25C4", "\u25C5", "\u25C6", "\u25C7",
    "\u25C8", "\u25C9", "\u25CA", "\u25CB", "\u25CC", "\u25CD", "\u25CE", "\u25CF",
    "\u25D0", "\u25D1", "\u25D2", "\u25D3", "\u25D4", "\u25D5", "\u25D6", "\u25D7",
    "\u25D8", "\u25D9", "\u25DA", "\u25DB", "\u25DC", "\u25DD", "\u25DE", "\u25DF",
]


class ShapesEncoder(Encoder):
    name = "Shapes"

    def encode(self, data: bytes) -> str:
        return bits_chunk_encode(data, _SHAPES, 6)

    def decode(self, text: str) -> bytes:
        return bits_chunk_decode(text, _SHAPES, 6)
