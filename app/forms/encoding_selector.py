from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItem, QStandardItemModel
from PyQt5.QtWidgets import QComboBox, QHBoxLayout, QLabel, QWidget

from ..encoding import ENCODERS


class EncodingSelector(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(QLabel("Encoding:"))
        self.combo = QComboBox()
        model = QStandardItemModel()
        for group_label in ["Standard", "Fun"]:
            items = [enc for enc in ENCODERS if enc.group == group_label]
            if items:
                group = QStandardItem(group_label)
                group.setFlags(Qt.NoItemFlags)
                group.setData(Qt.gray, Qt.ForegroundRole)
                model.appendRow(group)
                for enc in items:
                    model.appendRow(
                        QStandardItem(f"  {enc.name} ({enc.get_example()})")
                    )
        self.combo.setModel(model)
        hex_enc = next(e for e in ENCODERS if e.name.lower() == "hex")
        self.combo.setCurrentText(f"  {hex_enc.name} ({hex_enc.get_example()})")
        layout.addWidget(self.combo, 1)
