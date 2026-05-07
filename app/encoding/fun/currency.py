from ...base.encoder import Encoder

from .bits import bits_chunk_encode, bits_chunk_decode

_CURRENCY = [
    "$",
    "¢",
    "£",
    "¤",
    "¥",
    "₣",
    "₤",
    "₨",
    "₩",
    "₪",
    "₫",
    "€",
    "₱",
    "₲",
    "₹",
    "₺",
]


class CurrencyEncoder(Encoder):
    name = "Currency"

    def encode(self, data: bytes) -> str:
        return bits_chunk_encode(data, _CURRENCY, 4)

    def decode(self, text: str) -> bytes:
        return bits_chunk_decode(text, _CURRENCY, 4)
