from ...base.encoder import Encoder
from .bits import bits_chunk_encode, bits_chunk_decode

_SETS = [
    "∅",
    "∈",
    "∉",
    "∋",
    "⊂",
    "⊃",
    "⊄",
    "⊆",
    "⊇",
    "⊈",
    "∪",
    "∩",
    "∖",
    "×",
    "∆",
    "∀",
    "∃",
    "∄",
    "→",
    "↦",
    "∘",
    "⊥",
    "∁",
    "ℵ",
    "ℕ",
    "ℤ",
    "ℚ",
    "ℝ",
    "ℂ",
    "ℙ",
    "ℍ",
    "𝒫",
]


class SetEncoder(Encoder):
    name = "Set Theory"

    def encode(self, data: bytes) -> str:
        return bits_chunk_encode(data, _SETS, 5)

    def decode(self, text: str) -> bytes:
        return bits_chunk_decode(text, _SETS, 5)
