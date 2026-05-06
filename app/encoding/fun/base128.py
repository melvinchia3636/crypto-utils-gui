from ...base.encoder import Encoder

_ASCII = "".join(chr(i) for i in range(33, 127))
_EXTRA = "".join(chr(i) for i in range(192, 256))
_BASE128 = _ASCII + _EXTRA


class Base128Encoder(Encoder):
    name = "Base128"

    def encode(self, data: bytes) -> str:
        bits = "".join(f"{b:08b}" for b in data)
        result = []

        for i in range(0, len(bits), 7):
            chunk = bits[i : i + 7].ljust(7, "0")
            result.append(_BASE128[int(chunk, 2)])

        return "".join(result)

    def decode(self, text: str) -> bytes:
        rev = {c: i for i, c in enumerate(_BASE128)}
        bits = "".join(f"{rev[c]:07b}" for c in text.strip())
        result = []

        for i in range(0, len(bits), 8):
            chunk = bits[i : i + 8]
            if len(chunk) < 8:
                break
            result.append(int(chunk, 2))

        return bytes(result)
