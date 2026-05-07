from ...base.encoder import Encoder
from ..fun.bits import bits_chunk_encode, bits_chunk_decode

_CELLPHONE = ["\U0001F4F1", "\U0001F4F2", "\U0001F4DE", "\U0001F4DF", "\U0001F4E0", "\U0001F50B", "\U0001F50C", "\U0001F4F6"]


class CellPhoneEncoder(Encoder):
    name = "CellPhone"

    def encode(self, data: bytes) -> str:
        return bits_chunk_encode(data, _CELLPHONE, 3)

    def decode(self, text: str) -> bytes:
        return bits_chunk_decode(text, _CELLPHONE, 3)
