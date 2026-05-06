from base64 import b64encode, b64decode, b32encode, b32decode, b16encode, b16decode
from PyQt5.QtWidgets import QApplication


def current_encoding() -> str:
    for w in QApplication.topLevelWidgets():
        if hasattr(w, "encoding_combo"):
            return w.encoding_combo.currentText()
    return "hex"


def encode_bytes(data: bytes, encoding: str) -> str:
    if encoding == "hex":
        return data.hex()
    elif encoding == "base64":
        return b64encode(data).decode()
    elif encoding == "base32":
        return b32encode(data).decode()
    elif encoding == "base16":
        return b16encode(data).decode()
    else:
        raise ValueError(f"Unsupported encoding: {encoding}")


def decode_string(text: str, encoding: str) -> bytes:
    if encoding == "hex":
        return bytes.fromhex(text)
    elif encoding == "base64":
        return b64decode(text.encode())
    elif encoding == "base32":
        return b32decode(text.encode())
    elif encoding == "base16":
        return b16decode(text.encode())
    else:
        raise ValueError(f"Unsupported encoding: {encoding}")


def encode_string(data: str, encoding: str) -> str:
    return encode_bytes(data.encode(), encoding)
