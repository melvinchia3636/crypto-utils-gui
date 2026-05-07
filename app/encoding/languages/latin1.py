from ...base.encoder import Encoder

from ..fun.bits import bits_chunk_encode, bits_chunk_decode

_LATIN1 = [chr(cp) for cp in range(0x00C0, 0x0100)]


class Latin1Encoder(Encoder):
    name = "Latin-1"

    def encode(self, data: bytes) -> str:
        return bits_chunk_encode(data, _LATIN1, 6)

    def decode(self, text: str) -> bytes:
        return bits_chunk_decode(text, _LATIN1, 6)
