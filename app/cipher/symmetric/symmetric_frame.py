from ...helpers.algorithm_browser import AlgorithmBrowser
from ...helpers.discover_modules import discover_modules
import sys


class SymmetricWidget(AlgorithmBrowser):
    def __init__(self, parent=None):
        package = sys.modules[__package__]
        ciphers = discover_modules(package, attr_name="Cipher")
        entries = [(c.name, c) for c in ciphers]
        super().__init__(entries, listbox_label="Cipher Method", parent=parent)
