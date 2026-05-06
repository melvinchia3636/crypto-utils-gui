from ...helpers.algorithm_browser import AlgorithmBrowser
from . import aes, aes_file, blowfish, consolidated, des, des3, rc4
from . import twofish


class SymmetricWidget(AlgorithmBrowser):
    def __init__(self, parent=None):
        entries = [
            ("DES", des),
            ("3DES", des3),
            ("AES", aes),
            ("Blowfish", blowfish),
            ("Twofish", twofish),
            ("RC4", rc4),
            ("Symmetric (Consolidated)", consolidated),
            ("AES File", aes_file),
        ]
        super().__init__(entries, listbox_label="Cipher Method", parent=parent)
