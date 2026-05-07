from ...base.encoder import Encoder

_BASE36 = "0123456789abcdefghijklmnopqrstuvwxyz"


class Base36Encoder(Encoder):
    name = "Base36"

    def encode(self, data: bytes) -> str:
        num = int.from_bytes(data, "big")
        if num == 0:
            return _BASE36[0]

        chars = []

        while num > 0:
            num, rem = divmod(num, 36)
            chars.append(_BASE36[rem])

        return "".join(reversed(chars))

    def decode(self, text: str) -> bytes:
        num = 0

        for c in text.strip().lower():
            num = num * 36 + _BASE36.index(c)

        byte_len = (num.bit_length() + 7) // 8

        return num.to_bytes(byte_len, "big")
