from ...base.encoder import Encoder

_EMOJI_TABLE = [chr(0x1F300 + i) for i in range(256)]


class EmojiEncoder(Encoder):
    name = "Emoji"

    def encode(self, data: bytes) -> str:
        return "".join(_EMOJI_TABLE[b] for b in data)

    def decode(self, text: str) -> bytes:
        rev = {v: k for k, v in enumerate(_EMOJI_TABLE)}
        return bytes(rev[c] for c in text.strip())
