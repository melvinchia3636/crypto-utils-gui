from PyQt5.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QListWidget,
    QLabel,
    QScrollArea,
    QSplitter,
    QStackedWidget,
)
from PyQt5.QtCore import Qt


class AlgorithmBrowser(QWidget):
    def __init__(self, entries, listbox_label="Selector", parent=None):
        super().__init__(parent)
        self._entries = entries

        layout = QVBoxLayout(self)
        layout.setContentsMargins(16, 16, 16, 16)

        splitter = QSplitter(Qt.Horizontal)
        splitter.setChildrenCollapsible(False)
        splitter.setHandleWidth(16)

        left = QWidget()
        left_layout = QVBoxLayout(left)
        left_layout.setContentsMargins(0, 0, 0, 0)
        left_layout.setSpacing(8)
        lbl = QLabel(listbox_label)
        lbl.setStyleSheet("font-weight: bold; font-size: 16pt;")
        left_layout.addWidget(lbl)
        self.listbox = QListWidget()
        for name, _ in entries:
            self.listbox.addItem(name)
        left_layout.addWidget(self.listbox)
        splitter.addWidget(left)

        self.stack = QStackedWidget()
        for _, mod in entries:
            scroll = QScrollArea()
            scroll.setWidgetResizable(True)
            scroll.setFrameShape(QScrollArea.NoFrame)
            scroll.setStyleSheet("")
            pal = scroll.palette()
            pal.setColor(scroll.backgroundRole(), Qt.transparent)
            scroll.setPalette(pal)
            scroll.viewport().setPalette(pal)
            scroll.setWidget(mod.frame.Frame())
            self.stack.addWidget(scroll)

        splitter.addWidget(self.stack)
        splitter.setStretchFactor(0, 0)
        splitter.setStretchFactor(1, 1)
        splitter.setSizes([180, 600])

        layout.addWidget(splitter)

        self.listbox.currentRowChanged.connect(self.stack.setCurrentIndex)
        if self.stack.count():
            self.listbox.setCurrentRow(0)
