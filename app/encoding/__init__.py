import importlib
import pkgutil
from . import standard, fun
from .encoder import Encoder


def _discover_encoders(package, group_name):
    encoders = []
    for info in pkgutil.iter_modules(package.__path__):
        if info.name.startswith("_"):
            continue
        mod = importlib.import_module(f".{info.name}", package.__name__)
        for attr_name in dir(mod):
            attr = getattr(mod, attr_name)
            if isinstance(attr, type) and issubclass(attr, Encoder) and attr is not Encoder:
                inst = attr()
                inst.group = group_name
                encoders.append(inst)
    return encoders


ENCODERS = _discover_encoders(standard, "Standard") + _discover_encoders(fun, "Fun")
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
