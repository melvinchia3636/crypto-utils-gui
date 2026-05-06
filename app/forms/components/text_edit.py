from PyQt5.QtWidgets import QTextEdit

from ...base.form_component import FormComponent
from ..utils.builder_utils import row_col


class Component(FormComponent):
    name = "text"

    def build(self, layout, cfg):
        w = QTextEdit()
        w.setMinimumHeight(160)
        w.setMaximumHeight(160)
        if cfg.get("default"):
            w.setPlainText(cfg["default"])
        if cfg.get("readonly", False):
            w.setReadOnly(True)
            setattr(cfg["target"], f"{cfg['attr']}_widget", w)
        setattr(cfg["target"], cfg["attr"], w)
        layout.addWidget(w, *row_col(cfg))
