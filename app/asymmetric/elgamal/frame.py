from ...helpers.content_tab import TabbedFrame
from .frames.key_gen import KeyGenTab
from .frames.enc_dec import EncryptDecryptTab


class Frame(TabbedFrame):
    tab_specs = [
        (KeyGenTab, "Key Generation"),
        (EncryptDecryptTab, "Encryption / Decryption"),
    ]
