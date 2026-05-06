from PyQt5.QtWidgets import QPushButton, QFileDialog, QMessageBox
from ...base.form_component import FormComponent
from ..utils.builder_utils import row_col


class Component(FormComponent):
    name = "file_import_button"

    def build(self, layout, cfg):
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
                QMessageBox.critical(target, "Import Error", f"Failed to import: {e}")

        btn.clicked.connect(_do_import)
        layout.addWidget(btn, *row_col(cfg))
