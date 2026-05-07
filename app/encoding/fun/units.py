from ...base.encoder import Encoder
from .bits import bits_chunk_encode, bits_chunk_decode

_UNITS = [
    "㍱",
    "㍲",
    "㍳",
    "㍴",
    "㍵",
    "㍶",
    "㎀",
    "㎁",
    "㎂",
    "㎃",
    "㎄",
    "㎅",
    "㎆",
    "㎇",
    "㎈",
    "㎉",
    "㎊",
    "㎋",
    "㎌",
    "㎍",
    "㎎",
    "㎏",
    "㎐",
    "㎑",
    "㎒",
    "㎓",
    "㎔",
    "㎕",
    "㎖",
    "㎗",
    "㎘",
    "㎙",
]


class UnitsEncoder(Encoder):
    name = "Units"

    def encode(self, data: bytes) -> str:
        return bits_chunk_encode(data, _UNITS, 5)

    def decode(self, text: str) -> bytes:
        return bits_chunk_decode(text, _UNITS, 5)
