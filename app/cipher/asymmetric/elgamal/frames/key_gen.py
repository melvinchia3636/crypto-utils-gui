from PyQt5.QtWidgets import QMessageBox
from .....base.content_tab import ContentTab
from .....forms import FormBuilder
from .. import alg


KEY_SIZES = alg.KEY_SIZES


def _elgamal_import_pub(t, data):
    p, g, y = alg._import_pub(data)
    pub_pem = alg._serialize_pub(p, g, y)
    getattr(t, "kg_pub_widget").setPlainText(pub_pem)
    t._parent_frame._tabs.widget(1).enc_pubkey.setPlainText(pub_pem)
    t.pub_export_data = pub_pem


def _elgamal_import_priv(t, data):
    p, g, y, x = alg._import_priv(data)
    pub_pem = alg._serialize_pub(p, g, y)
    priv_pem = alg._serialize_priv(p, g, y, x)
    t._set_keys(pub_pem, priv_pem)


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
                "items": KEY_SIZES,
                "default": "256",
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
                "kind": "file_export_button",
                "row": 2,
                "col": 1,
                "colspan": 1,
                "target": self,
                "attr": "pub_export_data",
                "text": "Export",
                "dialog_title": "Export Public Key",
                "default_name": "public_key.pem",
                "file_filter": "PEM files (*.pem)",
            },
            {
                "kind": "file_import_button",
                "row": 2,
                "col": 2,
                "colspan": 1,
                "target": self,
                "attr": "pub_import_data",
                "text": "Import",
                "dialog_title": "Import Public Key",
                "default_name": "public_key.pem",
                "file_filter": "PEM files (*.pem)",
                "on_import": _elgamal_import_pub,
            },
            {
                "kind": "text",
                "row": 3,
                "col": 0,
                "colspan": 3,
                "target": self,
                "attr": "kg_pub",
                "readonly": True,
            },
            {"kind": "label", "row": 4, "col": 0, "text": "Private key:"},
            {
                "kind": "file_export_button",
                "row": 4,
                "col": 1,
                "colspan": 1,
                "target": self,
                "attr": "priv_export_data",
                "text": "Export",
                "dialog_title": "Export Private Key",
                "default_name": "private_key.pem",
                "file_filter": "PEM files (*.pem)",
            },
            {
                "kind": "file_import_button",
                "row": 4,
                "col": 2,
                "colspan": 1,
                "target": self,
                "attr": "priv_import_data",
                "text": "Import",
                "dialog_title": "Import Private Key",
                "default_name": "private_key.pem",
                "file_filter": "PEM files (*.pem)",
                "on_import": _elgamal_import_priv,
            },
            {
                "kind": "text",
                "row": 5,
                "col": 0,
                "colspan": 3,
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
            pub, priv = alg.generate_keypair(size)
            self._set_keys(pub, priv)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Key generation failed: {e}")

    def _set_keys(self, pub, priv):
        getattr(self, "kg_pub_widget").setPlainText(pub)
        getattr(self, "kg_priv_widget").setPlainText(priv)
        self.pub_export_data = pub
        self.priv_export_data = priv
        self.pub_import_data = pub
        self.priv_import_data = priv
        self._parent_frame._tabs.widget(1).enc_pubkey.setPlainText(pub)
        self._parent_frame._tabs.widget(1).dec_privkey.setPlainText(priv)
