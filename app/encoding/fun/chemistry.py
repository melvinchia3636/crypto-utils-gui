import os
from ...base.encoder import Encoder
from ..fun.bits import bits_chunk_encode, bits_chunk_decode

_CHEM = (
    [c for c in "ABCDEFGHIKLMNOPRSTUVWXYZ"] +
    [c for c in "abcdefghijklmnopqrstuvwxyz"] +
    [chr(0x2080 + i) for i in range(10)] +
    ["→", "+", "−", "·"]
)


def _add_noise(text):
    result = []
    i = 0
    while i < len(text):
        group_size = 2 + (ord(text[i]) % 3)
        group = text[i:i + group_size]
        if len(group) >= 2:
            result.append(f"({group})")
        else:
            result.append(group)
        i += group_size
    return "".join(result)


class ChemistryEncoder(Encoder):
    name = "Chemistry"

    def encode(self, data: bytes) -> str:
        result = bits_chunk_encode(data, _CHEM, 6)
        return _add_noise(result)

    def decode(self, text: str) -> bytes:
        cleaned = text.replace("(", "").replace(")", "")
        return bits_chunk_decode(cleaned, _CHEM, 6)
