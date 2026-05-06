from ..encoder import Encoder
from .bars import _bits_chunk_encode, _bits_chunk_decode

_TILES = "".join(chr(0x1F000 + i) for i in range(64))


class MahjongEncoder(Encoder):
    name = "Mahjong"

    def encode(self, data: bytes) -> str:
        return _bits_chunk_encode(data, _TILES, 6)

    def decode(self, text: str) -> bytes:
        return _bits_chunk_decode(text, _TILES, 6)
