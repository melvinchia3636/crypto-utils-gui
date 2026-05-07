from ...base.encoder import Encoder

from .bits import bits_chunk_encode, bits_chunk_decode

_MUSIC = ["♩", "♪", "♫", "♬", "♭", "♮", "♯", "𝄞"]


class MusicEncoder(Encoder):
    name = "Music"

    def encode(self, data: bytes) -> str:
        return bits_chunk_encode(data, _MUSIC, 3)

    def decode(self, text: str) -> bytes:
        return bits_chunk_decode(text, _MUSIC, 3)
