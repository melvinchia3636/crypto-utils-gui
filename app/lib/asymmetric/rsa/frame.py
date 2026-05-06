from ....helpers.content_tab import TabbedFrame
from .frames.key_gen import KeyGenTab
from .frames.enc_dec import EncryptDecryptTab
from .frames.sign_verify import SignVerifyTab


class Frame(TabbedFrame):
    tab_specs = [
        (KeyGenTab, "Key Generation"),
        (EncryptDecryptTab, "Encryption / Decryption (OAEP)"),
        (SignVerifyTab, "Signing / Verification (PSS)"),
    ]
