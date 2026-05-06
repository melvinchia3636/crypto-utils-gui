from ...base.encoder import Encoder


class OctalEncoder(Encoder):
    name = "Octal"

    def encode(self, data: bytes) -> str:
        return "".join(f"{b:03o}" for b in data)

    def decode(self, text: str) -> bytes:
        s = text.strip()
        return bytes(int(s[i : i + 3], 8) for i in range(0, len(s), 3))
