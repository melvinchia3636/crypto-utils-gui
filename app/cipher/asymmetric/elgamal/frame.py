from ....base.content_tab import TabbedFrame
from .frames.enc_dec import EncryptDecryptTab
from .frames.key_gen import KeyGenTab


class Frame(TabbedFrame):
    tab_specs = [
        (KeyGenTab, "Key Generation"),
        (EncryptDecryptTab, "Encryption / Decryption"),
    ]
