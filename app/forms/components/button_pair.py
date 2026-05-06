from PyQt5.QtWidgets import QHBoxLayout, QPushButton, QWidget

from ...base.form_component import FormComponent
from ..utils.builder_utils import row_col


class Component(FormComponent):
    name = "button_pair"

    def build(self, layout, cfg):
        container = QWidget()
        hbox = QHBoxLayout(container)
        hbox.setContentsMargins(0, 0, 0, 0)
        hbox.setSpacing(8)

        left = QPushButton(cfg["text_left"])
        left.clicked.connect(cfg["command_left"])

        right = QPushButton(cfg["text_right"])
        right.clicked.connect(cfg["command_right"])

        hbox.addWidget(left)
        hbox.addWidget(right)

        layout.addWidget(container, *row_col(cfg))
