from ..encoder import Encoder
from .bars import _bits_chunk_encode, _bits_chunk_decode

_MATH = "∑∆∇⊕⊗∞≈∫∏√∂∅∈∉∩∪⊂⊃∧∨¬⇒⇔∀∃∴≡≠≤≥⊥∠"


class MathEncoder(Encoder):
    name = "Math"

    def encode(self, data: bytes) -> str:
        return _bits_chunk_encode(data, _MATH, 5)

    def decode(self, text: str) -> bytes:
        return _bits_chunk_decode(text, _MATH, 5)
