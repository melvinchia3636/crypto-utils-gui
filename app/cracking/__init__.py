from PyQt5.QtWidgets import QScrollArea, QTabWidget, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt

from .tabs.brute_force_tab import BruteForceTab
from .tabs.dictionary_tab import DictionaryTab


def _wrap_scroll(widget):
    scroll = QScrollArea()
    scroll.setWidgetResizable(True)
    scroll.setAlignment(Qt.AlignTop)
    scroll.setFrameShape(QScrollArea.NoFrame)
    scroll.setAutoFillBackground(False)
    scroll.viewport().setAutoFillBackground(False)
    pal = scroll.viewport().palette()
    pal.setColor(scroll.viewport().backgroundRole(), Qt.transparent)
    scroll.viewport().setPalette(pal)
    scroll.setWidget(widget)
    return scroll


class CrackingTab(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        layout = QVBoxLayout(self)
        crack_tabs = QTabWidget(self)
        crack_tabs.addTab(_wrap_scroll(BruteForceTab()), "Brute Force")
        crack_tabs.addTab(_wrap_scroll(DictionaryTab()), "Dictionary")
        layout.addWidget(crack_tabs)
