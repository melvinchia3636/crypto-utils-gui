from ..base.encoder import Encoder
from ..helpers.discover_modules import discover_modules
from . import emojis, fun, languages, standard

ENCODERS = (
    discover_modules(
        standard, Encoder, init_fn=lambda i: setattr(i, "group", "Standard")
    )
    + discover_modules(fun, Encoder, init_fn=lambda i: setattr(i, "group", "Fun"))
    + discover_modules(emojis, Encoder, init_fn=lambda i: setattr(i, "group", "Emoji"))
    + discover_modules(languages, Encoder, init_fn=lambda i: setattr(i, "group", "Languages"))
)
ENCODER_MAP = {e.name.lower(): e for e in ENCODERS}


def encode_bytes_to_string(data: bytes) -> str:
    encoder = ENCODER_MAP.get(Encoder.current().lower())

    if encoder:
        return encoder.encode(data)

    raise ValueError(f"Unsupported encoding: {Encoder.current()}")


def decode_string_to_bytes(text: str) -> bytes:
    encoder = ENCODER_MAP.get(Encoder.current().lower())

    if encoder:
        return encoder.decode(text)

    raise ValueError(f"Unsupported encoding: {Encoder.current()}")
