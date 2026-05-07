from ...base.encoder import Encoder
from .bits import bits_chunk_encode, bits_chunk_decode

_CHECKMARKS = [
    "✓",
    "✔",
    "✕",
    "✖",
    "✗",
    "✘",
    "☑",
    "☒",
]


class CheckmarksEncoder(Encoder):
    name = "Checkmarks"

    def encode(self, data: bytes) -> str:
        return bits_chunk_encode(data, _CHECKMARKS, 3)

    def decode(self, text: str) -> bytes:
        return bits_chunk_decode(text, _CHECKMARKS, 3)
