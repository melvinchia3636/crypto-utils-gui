from PyQt5.QtWidgets import QTabWidget, QVBoxLayout, QWidget

from .cipher import CipheringTab
from .cracking import CrackingTab


class App(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Crypto Utility Tool")
        self.resize(1000, 700)

        layout = QVBoxLayout(self)

        root_tabs = QTabWidget(self)
        root_tabs.addTab(CipheringTab(self), "Ciphering")
        root_tabs.addTab(CrackingTab(self), "Cracking")
        layout.addWidget(root_tabs)
