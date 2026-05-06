from ...base.encoder import Encoder


class BinaryEncoder(Encoder):
    name = "Binary"

    def encode(self, data: bytes) -> str:
        return "".join(f"{b:08b}" for b in data)

    def decode(self, text: str) -> bytes:
        s = text.strip()

        return bytes(int(s[i : i + 8], 2) for i in range(0, len(s), 8))
