from ...base.encoder import Encoder
from ..fun.bits import bits_chunk_encode, bits_chunk_decode

_BIRDS = ["🐦", "🐧", "🐤", "🐣", "🐥", "🦅", "🦆", "🦉", "🦇", "🦢", "🦩", "🦚", "🦜", "🐓", "🕊", "🐔"]


class BirdsEncoder(Encoder):
    name = "Birds"

    def encode(self, data: bytes) -> str:
        return bits_chunk_encode(data, _BIRDS, 4)

    def decode(self, text: str) -> bytes:
        return bits_chunk_decode(text, _BIRDS, 4)
