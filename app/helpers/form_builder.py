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
    w.setMinimumHeight(160)
    w.setMaximumHeight(160)
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


def _build_file_save(layout, cfg):
    container = QWidget()
    hbox = QHBoxLayout(container)
    hbox.setContentsMargins(0, 0, 0, 0)
    entry = QLineEdit()
    hbox.addWidget(entry)
    browse = QPushButton("Browse...")
    dialog_title = cfg.get("dialog_title", "Save file")
    browse.clicked.connect(
        lambda _, e=entry, t=dialog_title: e.setText(
            QFileDialog.getSaveFileName(None, t)[0] or e.text()
        )
    )
    hbox.addWidget(browse)
    setattr(cfg["target"], cfg["attr"], entry)
    layout.addWidget(container, *_row_col(cfg))


def _build_button_pair(layout, cfg):
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


def _build_file_import_button(layout, cfg):
    btn = QPushButton(cfg.get("text", "Import"))
    target = cfg["target"]
    attr = cfg["attr"]
    title = cfg.get("dialog_title", "Import")
    filt = cfg.get("file_filter", "")
    def_name = cfg.get("default_name", "")
    on_import = cfg.get("on_import")

    def _do_import():
        path = QFileDialog.getOpenFileName(target, title, def_name, filt)[0]
        if not path:
            return
        try:
            data = open(path).read()
            setattr(target, attr, data)
            if on_import:
                on_import(target, data)
        except Exception as e:
            from PyQt5.QtWidgets import QMessageBox

            QMessageBox.critical(target, "Import Error", f"Failed to import: {e}")

    btn.clicked.connect(_do_import)
    layout.addWidget(btn, *_row_col(cfg))


def _build_file_export_button(layout, cfg):
    btn = QPushButton(cfg.get("text", "Export"))
    target = cfg["target"]
    attr = cfg["attr"]
    title = cfg.get("dialog_title", "Export")
    filt = cfg.get("file_filter", "")
    def_name = cfg.get("default_name", "")
    on_export = cfg.get("on_export")

    def _do_export():
        data = getattr(target, attr, "")
        if not data:
            return
        try:
            path = QFileDialog.getSaveFileName(target, title, def_name, filt)[0]
            if not path:
                return
            open(path, "w").write(data)
            if on_export:
                on_export(target, data)
        except Exception as e:
            from PyQt5.QtWidgets import QMessageBox

            QMessageBox.critical(target, "Export Error", f"Failed to export: {e}")

    btn.clicked.connect(_do_export)
    layout.addWidget(btn, *_row_col(cfg))
    layout.addWidget(btn, *_row_col(cfg))


_BUILDERS = {
    "label": _build_label,
    "entry": _build_entry,
    "text": _build_text,
    "button": _build_button,
    "file": _build_file,
    "file_save": _build_file_save,
    "button_pair": _build_button_pair,
    "file_import_button": _build_file_import_button,
    "file_export_button": _build_file_export_button,
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
