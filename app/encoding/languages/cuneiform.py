from ...base.encoder import Encoder
from ..fun.bits import bits_chunk_encode, bits_chunk_decode

_CUNEIFORM = [chr(0x12000 + i) for i in range(256)]


class CuneiformEncoder(Encoder):
    name = "Cuneiform"

    def encode(self, data: bytes) -> str:
        return bits_chunk_encode(data, _CUNEIFORM, 8)

    def decode(self, text: str) -> bytes:
        return bits_chunk_decode(text, _CUNEIFORM, 8)
