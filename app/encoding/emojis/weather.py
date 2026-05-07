from ...base.encoder import Encoder
from ..fun.bits import bits_chunk_encode, bits_chunk_decode

_WEATHER = ["\u2600", "\U0001F324", "\u26C5", "\u26C5", "\u2601", "\U0001F326", "\U0001F327", "\u26C8",
            "\U0001F329", "\U0001F32A", "\U0001F32B", "\u2744", "\u2614", "\u2602", "\u2603", "\u26A1"]


class WeatherEncoder(Encoder):
    name = "Weather"

    def encode(self, data: bytes) -> str:
        return bits_chunk_encode(data, _WEATHER, 4)

    def decode(self, text: str) -> bytes:
        return bits_chunk_decode(text, _WEATHER, 4)
