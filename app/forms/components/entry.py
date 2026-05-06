from PyQt5.QtWidgets import QLineEdit

from ...base.form_component import FormComponent
from ..utils.builder_utils import row_col


class Component(FormComponent):
    name = "entry"

    def build(self, layout, cfg):
        w = QLineEdit()

        if cfg.get("default"):
            w.setText(cfg["default"])

        if cfg.get("readonly", False):
            w.setReadOnly(True)
            setattr(cfg["target"], f"{cfg['attr']}_widget", w)

        setattr(cfg["target"], cfg["attr"], w)

        layout.addWidget(w, *row_col(cfg))
