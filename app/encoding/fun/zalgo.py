from ...base.encoder import Encoder
from .bits import bits_chunk_encode, bits_chunk_decode

_ZALGO = (
    [chr(cp) for cp in range(0x0300, 0x0315) if chr(cp).isprintable()]
    + [chr(cp) for cp in range(0x0316, 0x0342) if chr(cp).isprintable()]
    + [chr(cp) for cp in range(0x0348, 0x0370) if chr(cp).isprintable()]
    + [chr(cp) for cp in range(0x0591, 0x05A8) if chr(cp).isprintable()]
)


class ZalgoEncoder(Encoder):
    name = "Zalgo"

    def encode(self, data: bytes) -> str:
        return bits_chunk_encode(data, _ZALGO, 7)

    def decode(self, text: str) -> bytes:
        return bits_chunk_decode(text, _ZALGO, 7)
