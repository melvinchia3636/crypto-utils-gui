from ...base.encoder import Encoder
from ..fun.bits import bits_chunk_encode, bits_chunk_decode

_OGHAM = "ᚁᚂᚃᚄᚅᚆᚇᚈᚉᚊᚋᚌᚍᚎᚏᚐᚑ"


class OghamEncoder(Encoder):
    name = "Ogham"

    def encode(self, data: bytes) -> str:
        return bits_chunk_encode(data, _OGHAM, 4)

    def decode(self, text: str) -> bytes:
        return bits_chunk_decode(text, _OGHAM, 4)
