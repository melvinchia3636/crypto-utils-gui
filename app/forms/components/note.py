from PyQt5.QtWidgets import QLabel

from ...base.form_component import FormComponent
from ..utils.builder_utils import row_col


class Component(FormComponent):
    name = "note"

    def build(self, layout, cfg):
        note = QLabel(cfg["text"])
        note.setWordWrap(True)
        note.setStyleSheet("color: gray; font-size: 12pt; padding: 8px;")
        layout.addWidget(note, *row_col(cfg))
