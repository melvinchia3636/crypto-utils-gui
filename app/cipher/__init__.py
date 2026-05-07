from PyQt5.QtWidgets import QTabWidget, QVBoxLayout, QWidget

from ..helpers.algorithm_browser import AlgorithmBrowser
from ..forms.encoding_selector import EncodingSelector
from . import asymmetric, symmetric

TABS = [
    (symmetric, "Cipher Methods"),
    (asymmetric, "Algorithms"),
]


class CipheringTab(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        layout = QVBoxLayout(self)
        cipher_tabs = QTabWidget(self)
        self.encoding_selector = EncodingSelector(self)
        self.parent().encoding_selector = self.encoding_selector

        [
            cipher_tabs.addTab(
                AlgorithmBrowser.make_browser(pkg, lbl),
                pkg.__name__.split(".")[-1].capitalize(),
            )
            for (pkg, lbl) in TABS
        ]

        layout.addWidget(self.encoding_selector)
        layout.addWidget(cipher_tabs)
