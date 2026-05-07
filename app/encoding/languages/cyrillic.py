from ...base.encoder import Encoder
from ..fun.bits import bits_chunk_encode, bits_chunk_decode

_CYRILLIC = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"


class CyrillicEncoder(Encoder):
    name = "Cyrillic"

    def encode(self, data: bytes) -> str:
        return bits_chunk_encode(data, _CYRILLIC, 5)

    def decode(self, text: str) -> bytes:
        return bits_chunk_decode(text, _CYRILLIC, 5)
