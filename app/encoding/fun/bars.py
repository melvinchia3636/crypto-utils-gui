from ...base.encoder import Encoder


def _bits_chunk_encode(data, alphabet, bits):
    bitstr = "".join(f"{b:08b}" for b in data)
    result = []
    for i in range(0, len(bitstr), bits):
        chunk = bitstr[i : i + bits].ljust(bits, "0")
        result.append(alphabet[int(chunk, 2)])
    return "".join(result)


def _bits_chunk_decode(text, alphabet, bits):
    rev = {c: i for i, c in enumerate(alphabet)}
    bitstr = "".join(f"{rev[c]:0{bits}b}" for c in text.strip())
    return bytes(int(bitstr[i : i + 8], 2) for i in range(0, len(bitstr) - 7, 8))


_BARS = ["▁", "▂", "▃", "▄", "▅", "▆", "▇", "█"]


class BarsEncoder(Encoder):
    name = "Bars"

    def encode(self, data: bytes) -> str:
        return _bits_chunk_encode(data, _BARS, 3)

    def decode(self, text: str) -> bytes:
        return _bits_chunk_decode(text, _BARS, 3)
