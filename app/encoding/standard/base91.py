from ...base.encoder import Encoder

_BASE91 = (
    "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    "0123456789!#$%&()*+,./:;<=>?@[]^_`{|}~\""
)


class Base91Encoder(Encoder):
    name = "Base91"

    def encode(self, data: bytes) -> str:
        b, n, v = 0, 0, 0
        out = []

        for byte in data:
            b |= byte << n
            n += 8

            if n > 13:
                v = b & 8191
                if v > 88:
                    b >>= 13
                    n -= 13
                else:
                    v = b & 16383
                    b >>= 14
                    n -= 14

                out.append(_BASE91[v % 91])
                out.append(_BASE91[v // 91])

        if n:
            out.append(_BASE91[b % 91])
            if n > 7 or b > 90:
                out.append(_BASE91[b // 91])

        return "".join(out)

    def decode(self, text: str) -> bytes:
        v, b, n = -1, 0, 0
        out = bytearray()

        for c in text:
            idx = _BASE91.index(c)
            if v < 0:
                v = idx
            else:
                v += idx * 91
                b |= v << n
                n += 13 if (v & 8191) > 88 else 14

                while n > 7:
                    out.append(b & 255)
                    b >>= 8
                    n -= 8

                v = -1

        if v != -1:
            b |= v << n
            out.append(b & 255)

        return bytes(out)
