from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel as QtLabel

from ...base.form_component import FormComponent
from ..utils.builder_utils import row_col


class Component(FormComponent):
    name = "label"

    def build(self, layout, cfg):
        lbl = QtLabel(cfg["text"])

        layout.addWidget(lbl, *row_col(cfg), Qt.AlignTop)
