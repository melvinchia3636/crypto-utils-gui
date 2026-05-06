from ....helpers.content_tab import TabbedFrame
from .frames.key_gen import KeyGenTab
from .frames.enc_dec import EncryptDecryptTab
from app.encoding import (
    encode_bytes_to_string,
    decode_string_to_bytes,
)


class Frame(TabbedFrame):
    tab_specs = [
        (KeyGenTab, "Key Generation"),
        (EncryptDecryptTab, "Encryption / Decryption"),
    ]
