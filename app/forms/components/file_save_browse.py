from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLineEdit, QPushButton, QFileDialog
from ...base.form_component import FormComponent
from ..utils.builder_utils import row_col


class Component(FormComponent):
    name = "file_save"

    def build(self, layout, cfg):
        container = QWidget()
        hbox = QHBoxLayout(container)
        hbox.setContentsMargins(0, 0, 0, 0)
        entry = QLineEdit()
        hbox.addWidget(entry)
        browse = QPushButton("Browse...")
        dialog_title = cfg.get("dialog_title", "Save file")
        browse.clicked.connect(
            lambda _, e=entry, t=dialog_title: e.setText(
                QFileDialog.getSaveFileName(None, t)[0] or e.text()
            )
        )
        hbox.addWidget(browse)
        setattr(cfg["target"], cfg["attr"], entry)
        layout.addWidget(container, *row_col(cfg))
