from PyQt5.QtWidgets import QComboBox
from ...base.form_component import FormComponent
from ..utils.builder_utils import row_col


class Component(FormComponent):
    name = "combobox"

    def build(self, layout, cfg):
        w = QComboBox()
        items = cfg.get("items", [])
        for item in items:
            w.addItem(item)
        if cfg.get("default") is not None and cfg["default"] in items:
            w.setCurrentText(cfg["default"])
        w.currentTextChanged.connect(
            lambda text, t=cfg["target"], a=cfg["attr"]: setattr(t, a, text)
        )
        setattr(cfg["target"], cfg["attr"] + "_combo", w)
        setattr(cfg["target"], cfg["attr"], w.currentText())
        layout.addWidget(w, *row_col(cfg))
