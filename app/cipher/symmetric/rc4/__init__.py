from ....base.cipher_frame import CipherFrame
from . import frame

Cipher = CipherFrame("RC4", frame.Frame)
