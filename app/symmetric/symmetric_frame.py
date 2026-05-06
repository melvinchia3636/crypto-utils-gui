from ..helpers.algorithm_browser import AlgorithmBrowser
from . import des, aes, blowfish, twofish, rc4, aes_file, des3, consolidated


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
