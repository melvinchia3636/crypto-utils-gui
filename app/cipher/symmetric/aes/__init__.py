from ....base.cipher_frame import CipherFrame
from . import frame

Cipher = CipherFrame("AES", frame.Frame)
