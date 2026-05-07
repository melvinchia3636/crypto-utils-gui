from ...base.encoder import Encoder

from .bits import bits_chunk_encode, bits_chunk_decode

_BOLD = [
    "𝐀",
    "𝐁",
    "𝐂",
    "𝐃",
    "𝐄",
    "𝐅",
    "𝐆",
    "𝐇",
    "𝐈",
    "𝐉",
    "𝐊",
    "𝐋",
    "𝐌",
    "𝐍",
    "𝐎",
    "𝐏",
    "𝐐",
    "𝐑",
    "𝐒",
    "𝐓",
    "𝐔",
    "𝐕",
    "𝐖",
    "𝐗",
    "𝐘",
    "𝐙",
    "𝐚",
    "𝐛",
    "𝐜",
    "𝐝",
    "𝐞",
    "𝐟",
]


class BoldEncoder(Encoder):
    name = "Bold"

    def encode(self, data: bytes) -> str:
        return bits_chunk_encode(data, _BOLD, 5)

    def decode(self, text: str) -> bytes:
        return bits_chunk_decode(text, _BOLD, 5)
