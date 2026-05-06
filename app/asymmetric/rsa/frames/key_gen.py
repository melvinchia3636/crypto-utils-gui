from PyQt5.QtWidgets import QMessageBox
from ....helpers.content_tab import ContentTab
from ....helpers.form_builder import FormBuilder
from .. import alg


class KeyGenTab(ContentTab):
    def __init__(self, parent=None):
        super().__init__(parent, use_grid=True)
        config = [
            {"kind": "label", "row": 0, "col": 0, "text": "Key size (bits):"},
            {
                "kind": "combobox",
                "row": 0,
                "col": 1,
                "colspan": 2,
                "target": self,
                "attr": "kg_size",
                "items": alg.KEY_SIZES,
                "default": "2048",
            },
            {"kind": "label", "row": 1, "col": 0, "text": "Passphrase (optional):"},
            {
                "kind": "entry",
                "row": 1,
                "col": 1,
                "colspan": 2,
                "target": self,
                "attr": "kg_pass",
            },
            {
                "kind": "button",
                "row": 2,
                "col": 0,
                "colspan": 3,
                "text": "Generate Key Pair",
                "command": self._do_keygen,
            },
            {"kind": "label", "row": 3, "col": 0, "text": "Public key:"},
            {
                "kind": "text",
                "row": 3,
                "col": 1,
                "colspan": 2,
                "target": self,
                "attr": "kg_pub",
                "readonly": True,
            },
            {"kind": "label", "row": 4, "col": 0, "text": "Private key:"},
            {
                "kind": "text",
                "row": 4,
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
            size = int(self.kg_size)
            passphrase = self.kg_pass.text().strip() or None
            pub, priv = alg.generate_keypair(size, passphrase)
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
