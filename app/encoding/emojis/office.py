from ...base.encoder import Encoder
from ..fun.bits import bits_chunk_encode, bits_chunk_decode

_OFFICE = ["📎", "📏", "📐", "✂", "📍", "📌", "📋", "📁", "📂", "🗂", "📅", "📆", "📇", "📈", "📉", "📊"]


class OfficeEncoder(Encoder):
    name = "Office"

    def encode(self, data: bytes) -> str:
        return bits_chunk_encode(data, _OFFICE, 4)

    def decode(self, text: str) -> bytes:
        return bits_chunk_decode(text, _OFFICE, 4)
