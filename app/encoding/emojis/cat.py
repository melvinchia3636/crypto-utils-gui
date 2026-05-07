from ...base.encoder import Encoder
from ..fun.bits import bits_chunk_encode, bits_chunk_decode

_CATS = ["\U0001F63A", "\U0001F638", "\U0001F639", "\U0001F63B", "\U0001F63C", "\U0001F63D", "\U0001F640", "\U0001F63F", "\U0001F63E"]


class CatEncoder(Encoder):
    name = "Cat"

    def encode(self, data: bytes) -> str:
        return bits_chunk_encode(data, _CATS[:8], 3)

    def decode(self, text: str) -> bytes:
        return bits_chunk_decode(text, _CATS[:8], 3)
