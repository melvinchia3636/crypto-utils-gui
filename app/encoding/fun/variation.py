from ...base.encoder import Encoder

_VS = [chr(cp) for cp in range(0xFE00, 0xFE10)] + [chr(cp) for cp in range(0xE0100, 0xE01F0)]


class VariationEncoder(Encoder):
    name = "Variation"

    def encode(self, data: bytes) -> str:
        return "\u2588" + "".join(_VS[b] for b in data)

    def decode(self, text: str) -> bytes:
        result = bytearray()
        for ch in text:
            if ch in _VS:
                result.append(_VS.index(ch))
        return bytes(result)
