from ...base.encoder import Encoder
from ..fun.bits import bits_chunk_encode, bits_chunk_decode

_CANDY = ["\U0001F36C", "\U0001F36D", "\U0001F36B", "\U0001F36A", "\U0001F369", "\U0001F36E", "\U0001F382", "\U0001F370"]


class CandyEncoder(Encoder):
    name = "Candy"

    def encode(self, data: bytes) -> str:
        return bits_chunk_encode(data, _CANDY, 3)

    def decode(self, text: str) -> bytes:
        return bits_chunk_decode(text, _CANDY, 3)
