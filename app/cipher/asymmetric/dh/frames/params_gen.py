from PyQt5.QtWidgets import QMessageBox
from .....helpers.content_tab import ContentTab
from .....helpers.form_builder import FormBuilder
from .. import alg


class ParamsGenTab(ContentTab):
    def __init__(self, parent=None):
        super().__init__(parent, use_grid=True)
        config = [
            {"kind": "label", "row": 0, "col": 0, "text": "Key size:"},
            {
                "kind": "combobox",
                "row": 0,
                "col": 1,
                "colspan": 2,
                "target": self,
                "attr": "params_size",
                "items": alg.KEY_SIZES,
                "default": "2048",
            },
            {
                "kind": "button",
                "row": 1,
                "col": 0,
                "colspan": 3,
                "text": "Generate Parameters",
                "command": self._do_gen_params,
            },
            {"kind": "label", "row": 2, "col": 0, "text": "Parameters (PEM):"},
            {
                "kind": "text",
                "row": 2,
                "col": 1,
                "colspan": 2,
                "target": self,
                "attr": "params_pem",
                "readonly": True,
            },
        ]
        FormBuilder.build_single_section(self._grid, config)
        self._layout.addStretch()

    def _do_gen_params(self):
        try:
            size = int(self.params_size)
            params = alg.generate_params(size)
            pem = alg.params_to_pem(params)
            getattr(self, "params_pem_widget").setPlainText(pem)
            self._parent_frame._tabs.widget(1).kg_params.setPlainText(pem)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Parameter generation failed: {e}")
