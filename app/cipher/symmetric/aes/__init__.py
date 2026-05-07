from ....base.cipher_frame import CipherFrame
from . import frame

Cipher = CipherFrame("AES (AES-128-GCM)", frame.Frame)
