from urllib.parse import quote, unquote

from ...base.encoder import Encoder


class PercentEncoder(Encoder):
    name = "Percent"

    def encode(self, data: bytes) -> str:
        return quote(data, safe="")

    def decode(self, text: str) -> bytes:
        return unquote(text).encode("latin-1")
