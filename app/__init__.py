from PyQt5.QtWidgets import QTabWidget, QVBoxLayout, QWidget

from .cipher import asymmetric, symmetric
from .forms.encoding_selector import EncodingSelector
from .helpers.algorithm_browser import AlgorithmBrowser

TABS = [
    (symmetric, "Cipher Methods"),
    (asymmetric, "Algorithms"),
]


class App(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Crypto Utility Tool")
        self.resize(1000, 700)

        layout = QVBoxLayout(self)
        tabs = QTabWidget(self)

        [
            tabs.addTab(
                AlgorithmBrowser.make_browser(pkg, lbl),
                pkg.__name__.split(".")[-1].capitalize(),
            )
            for (pkg, lbl) in TABS
        ]

        layout.addWidget(EncodingSelector())
        layout.addWidget(tabs)
