from ...helpers.algorithm_browser import AlgorithmBrowser
from . import dh, ecc, elgamal
from . import rsa


class AsymmetricWidget(AlgorithmBrowser):
    def __init__(self, parent=None):
        entries = [
            ("RSA", rsa),
            ("ECC", ecc),
            ("Diffie-Hellman", dh),
            ("ElGamal", elgamal),
        ]
        super().__init__(entries, listbox_label="Algorithm", parent=parent)
