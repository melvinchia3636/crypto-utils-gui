from ...base.encoder import Encoder
from ..fun.bits import bits_chunk_encode, bits_chunk_decode

_HEARTS = ["❤", "🧡", "💛", "💚", "💙", "💜", "🤎", "🖤", "🤍", "💔", "❣", "💕", "💞", "💗", "💖", "💘"]


class HeartsEncoder(Encoder):
    name = "Hearts"

    def encode(self, data: bytes) -> str:
        return bits_chunk_encode(data, _HEARTS, 4)

    def decode(self, text: str) -> bytes:
        return bits_chunk_decode(text, _HEARTS, 4)
