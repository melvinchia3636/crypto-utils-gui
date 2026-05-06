from PyQt5.QtWidgets import QFileDialog, QMessageBox, QPushButton

from ...base.form_component import FormComponent
from ..utils.builder_utils import row_col


class Component(FormComponent):
    name = "file_export_button"

    def build(self, layout, cfg):
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
                QMessageBox.critical(target, "Export Error", f"Failed to export: {e}")

        btn.clicked.connect(_do_export)
        layout.addWidget(btn, *row_col(cfg))
