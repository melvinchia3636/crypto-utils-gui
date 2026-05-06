from PyQt5.QtWidgets import QFrame, QGridLayout, QLabel

from .components import BUILDERS


class FormBuilder:
    @staticmethod
    def build_single_section(layout, config):
        for cfg in config:
            kind = cfg.get("kind", "entry")
            builder = BUILDERS.get(kind)
            if builder:
                builder(layout, cfg)

    @staticmethod
    def build_multi_sections(container, tabs):
        for i, (title, config) in enumerate(tabs):
            if i > 0:
                line = QFrame()
                line.setFrameShape(QFrame.HLine)
                line.setFrameShadow(QFrame.Sunken)
                container.layout().addWidget(line)
            lbl = QLabel(title)
            lbl.setContentsMargins(12, 0, 12, 0)
            lbl.setStyleSheet("font-weight: bold; font-size: 16pt;")
            container.layout().addWidget(lbl)
            gl = QGridLayout()
            gl.setContentsMargins(12, 0, 12, 0)
            container.layout().addLayout(gl)
            FormBuilder.build_single_section(gl, config)
        container.layout().addStretch()
