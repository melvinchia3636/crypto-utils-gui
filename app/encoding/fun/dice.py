from ...base.encoder import Encoder
from .bits import bits_chunk_encode, bits_chunk_decode

_DICE = ["⚀", "⚁", "⚂", "⚃"]


class DiceEncoder(Encoder):
    name = "Dice"

    def encode(self, data: bytes) -> str:
        return bits_chunk_encode(data, _DICE, 2)

    def decode(self, text: str) -> bytes:
        return bits_chunk_decode(text, _DICE, 2)
