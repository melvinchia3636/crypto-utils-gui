from PyQt5.QtWidgets import QPushButton
from ...base.form_component import FormComponent
from ..utils.builder_utils import row_col


class Component(FormComponent):
    name = "button"

    def build(self, layout, cfg):
        btn = QPushButton(cfg["text"])
        btn.clicked.connect(cfg["command"])
        layout.addWidget(btn, *row_col(cfg))
