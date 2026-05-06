from PyQt5.QtWidgets import (
    QApplication,
    QTabWidget,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QComboBox,
)
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtCore import Qt
from .lib.symmetric.symmetric_frame import SymmetricWidget
from .lib.asymmetric.asymmetric_frame import AsymmetricWidget
from .encoding import ENCODERS
import sys

_groups = {}
for enc in ENCODERS:
    _groups.setdefault(enc.group, []).append(enc.name)


def _add_group(combo, model, label, items):
    group = QStandardItem(label)
    group.setFlags(Qt.NoItemFlags)
    group.setData(Qt.gray, Qt.ForegroundRole)
    model.appendRow(group)
    for item in items:
        display = f"  {item.name} ({item.get_example()})"
        model.appendRow(QStandardItem(display))


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Crypto Utility Tool")
        self.resize(1000, 700)

        layout = QVBoxLayout(self)
        top_bar = QHBoxLayout()
        top_bar.addWidget(QLabel("Encoding:"))
        self.encoding_combo = QComboBox()
        model = QStandardItemModel()
        for group_label in ["Standard", "Fun"]:
            items = [enc for enc in ENCODERS if enc.group == group_label]
            if items:
                _add_group(self.encoding_combo, model, group_label, items)
        self.encoding_combo.setModel(model)
        hex_enc = next(e for e in ENCODERS if e.name.lower() == "hex")
        self.encoding_combo.setCurrentText(f"  {hex_enc.name} ({hex_enc.get_example()})")
        top_bar.addWidget(self.encoding_combo, 1)
        layout.addLayout(top_bar)
        tabs = QTabWidget()
        tabs.addTab(SymmetricWidget(), "Symmetric")
        tabs.addTab(AsymmetricWidget(), "Asymmetric")
        layout.addWidget(tabs)


def main():
    app = QApplication(sys.argv)
    w = App()
    w.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
