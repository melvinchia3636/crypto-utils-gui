from PyQt5.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QTextEdit,
    QFrame,
    QGridLayout,
    QFileDialog,
    QComboBox,
)
from PyQt5.QtCore import Qt


def _row_col(cfg):
    return cfg["row"], cfg["col"], 1, cfg.get("colspan", 1)


def _build_label(layout, cfg):
    lbl = QLabel(cfg["text"])
    layout.addWidget(lbl, *_row_col(cfg), Qt.AlignTop)


def _build_entry(layout, cfg):
    w = QLineEdit()
    if cfg.get("default"):
        w.setText(cfg["default"])
    if cfg.get("readonly", False):
        w.setReadOnly(True)
        setattr(cfg["target"], f"{cfg['attr']}_widget", w)
    setattr(cfg["target"], cfg["attr"], w)
    layout.addWidget(w, *_row_col(cfg))


def _build_text(layout, cfg):
    w = QTextEdit()
    w.setMaximumHeight(100)
    if cfg.get("default"):
        w.setPlainText(cfg["default"])
    if cfg.get("readonly", False):
        w.setReadOnly(True)
        setattr(cfg["target"], f"{cfg['attr']}_widget", w)
    setattr(cfg["target"], cfg["attr"], w)
    layout.addWidget(w, *_row_col(cfg))


def _build_button(layout, cfg):
    btn = QPushButton(cfg["text"])
    btn.clicked.connect(cfg["command"])
    layout.addWidget(btn, *_row_col(cfg))


def _build_file(layout, cfg):
    container = QWidget()
    hbox = QHBoxLayout(container)
    hbox.setContentsMargins(0, 0, 0, 0)
    entry = QLineEdit()
    hbox.addWidget(entry)
    browse = QPushButton("Browse...")
    dialog_title = cfg.get("dialog_title", "Select file")
    browse.clicked.connect(
        lambda _, e=entry, t=dialog_title: e.setText(
            QFileDialog.getOpenFileName(None, t)[0] or e.text()
        )
    )
    hbox.addWidget(browse)
    setattr(cfg["target"], cfg["attr"], entry)
    layout.addWidget(container, *_row_col(cfg))


def _build_combobox(layout, cfg):
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
    layout.addWidget(w, *_row_col(cfg))


_BUILDERS = {
    "label": _build_label,
    "entry": _build_entry,
    "text": _build_text,
    "button": _build_button,
    "file": _build_file,
    "combobox": _build_combobox,
}


class FormBuilder:
    @staticmethod
    def build_single_section(layout, config):
        for cfg in config:
            kind = cfg.get("kind", "entry")
            builder = _BUILDERS.get(kind)
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
            lbl.setStyleSheet("font-weight: bold; font-size: 16pt;")
            container.layout().addWidget(lbl)
            gl = QGridLayout()
            container.layout().addLayout(gl)
            FormBuilder.build_single_section(gl, config)
        container.layout().addStretch()
