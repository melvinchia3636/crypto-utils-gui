from ...base.encoder import Encoder
from ..fun.bits import bits_chunk_encode, bits_chunk_decode

_KEYCAPS = ["0️⃣", "1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣"]


class KeycapsEncoder(Encoder):
    name = "Keycaps"

    def encode(self, data: bytes) -> str:
        return bits_chunk_encode(data, _KEYCAPS, 3)

    def decode(self, text: str) -> bytes:
        return bits_chunk_decode(text, _KEYCAPS, 3)
