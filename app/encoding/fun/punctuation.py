from ...base.encoder import Encoder

from .bits import bits_chunk_encode, bits_chunk_decode

_PUNCT = [
    "!",
    '"',
    "#",
    "$",
    "%",
    "&",
    "'",
    "(",
    ")",
    "*",
    "+",
    ",",
    "-",
    ".",
    "/",
    ":",
    ";",
    "<",
    "=",
    ">",
    "?",
    "[",
    "\\",
    "]",
    "^",
    "_",
    "{",
    "|",
    "}",
    "~",
    "¡",
    "¿",
]


class PunctEncoder(Encoder):
    name = "Punctuation"

    def encode(self, data: bytes) -> str:
        return bits_chunk_encode(data, _PUNCT, 5)

    def decode(self, text: str) -> bytes:
        return bits_chunk_decode(text, _PUNCT, 5)
