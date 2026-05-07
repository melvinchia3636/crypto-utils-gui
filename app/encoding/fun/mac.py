from ...base.encoder import Encoder
from .bits import bits_chunk_encode, bits_chunk_decode

_MAC = ["⌃", "⌥", "⌘", "⎋", "⏏", "⇧", "⇪", "⌫", "⌦", "↩", "⇥", "⌤", "⇭", "⌧", "⌅", "⌆"]


class MacEncoder(Encoder):
    name = "Mac"

    def encode(self, data: bytes) -> str:
        return bits_chunk_encode(data, _MAC, 4)

    def decode(self, text: str) -> bytes:
        return bits_chunk_decode(text, _MAC, 4)
