from PyQt5.QtWidgets import QTabWidget, QVBoxLayout, QWidget

from .cipher import asymmetric, symmetric
from .forms.encoding_selector import EncodingSelector
from .helpers.algorithm_browser import AlgorithmBrowser


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Crypto Utility Tool")
        self.resize(1000, 700)

        layout = QVBoxLayout(self)
        self.encoding_selector = EncodingSelector()
        layout.addWidget(self.encoding_selector)
        tabs = QTabWidget()
        tabs.addTab(
            AlgorithmBrowser.make_browser(symmetric, "Cipher Methods"), "Symmetric"
        )
        tabs.addTab(
            AlgorithmBrowser.make_browser(asymmetric, "Algorithms"), "Asymmetric"
        )
        layout.addWidget(tabs)
