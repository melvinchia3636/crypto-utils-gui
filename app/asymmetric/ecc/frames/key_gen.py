from PyQt5.QtWidgets import QMessageBox
from ....helpers.content_tab import ContentTab
from ....helpers.form_builder import FormBuilder
from .. import alg


CURVES = ["P-256", "P-384", "P-521"]


class KeyGenTab(ContentTab):
    def __init__(self, parent=None):
        super().__init__(parent, use_grid=True)
        config = [
            {"kind": "label", "row": 0, "col": 0, "text": "Curve:"},
            {
                "kind": "combobox",
                "row": 0,
                "col": 1,
                "colspan": 2,
                "target": self,
                "attr": "kg_curve",
                "items": CURVES,
                "default": "P-256",
            },
            {
                "kind": "button",
                "row": 1,
                "col": 0,
                "colspan": 3,
                "text": "Generate Key Pair",
                "command": self._do_keygen,
            },
            {"kind": "label", "row": 2, "col": 0, "text": "Public key:"},
            {
                "kind": "text",
                "row": 2,
                "col": 1,
                "colspan": 2,
                "target": self,
                "attr": "kg_pub",
                "readonly": True,
            },
            {"kind": "label", "row": 3, "col": 0, "text": "Private key:"},
            {
                "kind": "text",
                "row": 3,
                "col": 1,
                "colspan": 2,
                "target": self,
                "attr": "kg_priv",
                "readonly": True,
            },
        ]
        FormBuilder.build_single_section(self._grid, config)
        self._layout.addStretch()

    def _do_keygen(self):
        try:
            curve = self.kg_curve
            pub, priv = alg.generate_keypair(curve)
            getattr(self, "kg_pub_widget").setPlainText(pub)
            getattr(self, "kg_priv_widget").setPlainText(priv)
            enc_tab = self._parent_frame._tabs.widget(1)
            enc_tab.enc_pubkey.setPlainText(pub)
            enc_tab.dec_privkey.setPlainText(priv)
            sign_tab = self._parent_frame._tabs.widget(2)
            sign_tab.sign_privkey.setPlainText(priv)
            sign_tab.verify_pubkey.setPlainText(pub)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Key generation failed: {e}")
