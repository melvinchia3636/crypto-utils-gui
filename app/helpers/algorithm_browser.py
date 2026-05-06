from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QLabel,
    QListWidget,
    QScrollArea,
    QSplitter,
    QStackedWidget,
    QVBoxLayout,
    QWidget,
)

from .discover_modules import discover_modules


class AlgorithmBrowser(QWidget):
    def __init__(self, entries, listbox_label="Selector", parent=None):
        super().__init__(parent)

        self._entries = entries
        self._listbox_label = listbox_label

        self.listbox = QListWidget()
        self.stack = QStackedWidget()

        self._build_ui()

    def _build_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(16, 16, 16, 16)

        splitter = self._build_splitter()
        layout.addWidget(splitter)

    def _build_splitter(self):
        splitter = QSplitter(Qt.Horizontal)
        splitter.setChildrenCollapsible(False)
        splitter.setHandleWidth(16)

        splitter.addWidget(self._build_left_panel())
        splitter.addWidget(self._build_right_stack())

        splitter.setStretchFactor(0, 0)
        splitter.setStretchFactor(1, 1)
        splitter.setSizes([180, 600])

        return splitter

    def _build_left_panel(self):
        left = QWidget()

        layout = QVBoxLayout(left)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(8)

        lbl = QLabel(self._listbox_label)
        lbl.setStyleSheet("font-weight: bold; font-size: 16pt;")
        layout.addWidget(lbl)

        for name, _ in self._entries:
            self.listbox.addItem(name)

        layout.addWidget(self.listbox)

        return left

    def _build_right_stack(self):
        for _, entry in self._entries:
            self.stack.addWidget(self._build_scrollable(entry))

        self.listbox.currentRowChanged.connect(self.stack.setCurrentIndex)

        if self.stack.count():
            self.listbox.setCurrentRow(0)

        return self.stack

    def _build_scrollable(self, entry):
        scrollable = QScrollArea()
        scrollable.setWidgetResizable(True)
        scrollable.setAlignment(Qt.AlignTop)
        scrollable.setFrameShape(QScrollArea.NoFrame)
        scrollable.setStyleSheet("")

        pal = scrollable.palette()
        pal.setColor(scrollable.backgroundRole(), Qt.transparent)
        scrollable.setPalette(pal)
        scrollable.viewport().setPalette(pal)

        if hasattr(entry, "frame_class"):
            frame = entry.frame_class()
        else:
            frame = entry.frame.Frame()

        scrollable.setWidget(frame)

        return scrollable

    @staticmethod
    def make_browser(package, label):
        ciphers = discover_modules(package, attr_name="Cipher")

        entries = [(c.name, c) for c in ciphers]

        return AlgorithmBrowser(entries, listbox_label=label)
