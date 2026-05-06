from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItem, QStandardItemModel
from PyQt5.QtWidgets import QComboBox, QHBoxLayout, QLabel, QWidget

from ..encoding import ENCODERS


class EncodingSelector(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        self.combo = QComboBox()
        self.combo.setModel(self._build_model())
        self.combo.setCurrentText(self._default_selection())

        layout.addWidget(QLabel("Encoding:"))
        layout.addWidget(self.combo, 1)

    def _build_model(self):
        model = QStandardItemModel()

        for group_label in list(dict.fromkeys([enc.group for enc in ENCODERS])):
            items = [enc for enc in ENCODERS if enc.group == group_label]

            if not items:
                continue

            group = QStandardItem(group_label)
            group.setFlags(Qt.NoItemFlags)
            group.setData(Qt.gray, Qt.ForegroundRole)
            model.appendRow(group)

            for enc in items:
                model.appendRow(QStandardItem(f"  {enc.name} ({enc.get_example()})"))

        return model

    def _default_selection(self):
        hex_enc = next(e for e in ENCODERS if e.name.lower() == "hex")

        return f"  {hex_enc.name} ({hex_enc.get_example()})"
