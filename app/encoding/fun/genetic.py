from ...base.encoder import Encoder
from .bits import bits_chunk_encode, bits_chunk_decode

_DNA = ["A", "C", "G", "T"]


class GeneticEncoder(Encoder):
    name = "Genetic"

    def encode(self, data: bytes) -> str:
        return bits_chunk_encode(data, _DNA, 2)

    def decode(self, text: str) -> bytes:
        return bits_chunk_decode(text, _DNA, 2)
