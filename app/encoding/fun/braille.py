from ...base.encoder import Encoder


class BrailleEncoder(Encoder):
    name = "Braille"
    _START = 0x2800

    def encode(self, data: bytes) -> str:
        return "".join(chr(self._START + b) for b in data)

    def decode(self, text: str) -> bytes:
        return bytes(ord(c) - self._START for c in text.strip())
