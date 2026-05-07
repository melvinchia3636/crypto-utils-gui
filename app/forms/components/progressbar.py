from PyQt5.QtWidgets import QLabel, QProgressBar, QVBoxLayout, QWidget

from ...base.form_component import FormComponent
from ..utils.builder_utils import row_col


class Component(FormComponent):
    name = "progressbar"

    def build(self, layout, cfg):
        container = QWidget()
        vbox = QVBoxLayout(container)
        vbox.setContentsMargins(0, 0, 0, 0)
        vbox.setSpacing(0)

        bar = QProgressBar()
        bar.setFormat(cfg.get("format", "%p% (%v/%m keys)"))
        vbox.addWidget(bar)

        label = QLabel("")
        label.setStyleSheet("color: gray; font-size: 10pt;")
        vbox.addWidget(label)

        setattr(cfg["target"], cfg["attr"], bar)
        setattr(cfg["target"], cfg["attr"] + "_label", label)
        setattr(cfg["target"], cfg["attr"] + "_container", container)

        layout.addWidget(container, *row_col(cfg))
