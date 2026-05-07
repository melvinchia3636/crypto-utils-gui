from ...base.encoder import Encoder
from ..fun.bits import bits_chunk_encode, bits_chunk_decode

_GOTHIC = "𐌰𐌱𐌲𐌳𐌴𐌵𐌶𐌷𐌸𐌹𐌺𐌻𐌼𐌽𐌾𐌿𐍀"


class GothicEncoder(Encoder):
    name = "Gothic"

    def encode(self, data: bytes) -> str:
        return bits_chunk_encode(data, _GOTHIC, 4)

    def decode(self, text: str) -> bytes:
        return bits_chunk_decode(text, _GOTHIC, 4)
