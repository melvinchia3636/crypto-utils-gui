from ...base.encoder import Encoder

from .bits import bits_chunk_encode, bits_chunk_decode

_ARROWS = []
for cp in range(0x2190, 0x2200):
    c = chr(cp)
    if len(c) == 1:
        _ARROWS.append(c)
for cp in range(0x2B00, 0x2B20):
    c = chr(cp)
    if len(c) == 1:
        _ARROWS.append(c)
for cp in range(0x27F0, 0x2800):
    c = chr(cp)
    if len(c) == 1:
        _ARROWS.append(c)

_ARROWS = _ARROWS[:128]


class ArrowEncoder(Encoder):
    name = "Arrows"

    def encode(self, data: bytes) -> str:
        return bits_chunk_encode(data, _ARROWS, 7)

    def decode(self, text: str) -> bytes:
        return bits_chunk_decode(text, _ARROWS, 7)
