from ...base.encoder import Encoder

from .bits import bits_chunk_encode, bits_chunk_decode

_CONTROL = [chr(0x2400 + i) for i in range(32)]


class ControlEncoder(Encoder):
    name = "Control"

    def encode(self, data: bytes) -> str:
        return bits_chunk_encode(data, _CONTROL, 5)

    def decode(self, text: str) -> bytes:
        return bits_chunk_decode(text, _CONTROL, 5)
