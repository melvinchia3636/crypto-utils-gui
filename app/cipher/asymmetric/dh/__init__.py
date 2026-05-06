from ....base.cipher_frame import CipherFrame
from . import frame

Cipher = CipherFrame("Diffie-Hellman", frame.Frame)
