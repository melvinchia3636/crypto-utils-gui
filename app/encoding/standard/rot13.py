from ...base.encoder import Encoder

_ROT13 = str.maketrans(
    "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz",
    "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm",
)

_ROT47 = str.maketrans(
    r"""!"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~""",
    r"""PQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~!"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNO""",
)


class ROT13Encoder(Encoder):
    name = "ROT13"

    def encode(self, data: bytes) -> str:
        return data.decode("latin-1").translate(_ROT13)

    def decode(self, text: str) -> bytes:
        return text.translate(_ROT13).encode("latin-1")


class ROT47Encoder(Encoder):
    name = "ROT47"

    def encode(self, data: bytes) -> str:
        return data.decode("latin-1").translate(_ROT47)

    def decode(self, text: str) -> bytes:
        return text.translate(_ROT47).encode("latin-1")
