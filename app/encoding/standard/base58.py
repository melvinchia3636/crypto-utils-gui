from ...base.encoder import Encoder

_BASE58 = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"


class Base58Encoder(Encoder):
    name = "Base58"

    def encode(self, data: bytes) -> str:
        num = int.from_bytes(data, "big")
        if num == 0:
            return _BASE58[0]
        chars = []
        while num > 0:
            num, rem = divmod(num, 58)
            chars.append(_BASE58[rem])
        return "".join(reversed(chars))

    def decode(self, text: str) -> bytes:
        num = 0
        for c in text.strip():
            num = num * 58 + _BASE58.index(c)
        byte_len = (num.bit_length() + 7) // 8
        return num.to_bytes(byte_len, "big")
