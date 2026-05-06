from PyQt5.QtWidgets import QMessageBox
from .....helpers.key_derivation import DEFAULT_PLAINTEXT
from .....base.content_tab import ContentTab
from .....forms import FormBuilder
from app.encoding import (
    encode_bytes_to_string,
    decode_string_to_bytes,
)
from .. import alg


class EncryptDecryptTab(ContentTab):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._layout.setContentsMargins(16, 16, 16, 16)
        enc_config = [
            {
                "kind": "label",
                "row": 0,
                "col": 0,
                "text": "Recipient public key (PEM):",
            },
            {
                "kind": "text",
                "row": 0,
                "col": 1,
                "colspan": 2,
                "target": self,
                "attr": "enc_pubkey",
            },
            {"kind": "label", "row": 1, "col": 0, "text": "Plaintext:"},
            {
                "kind": "text",
                "row": 1,
                "col": 1,
                "colspan": 2,
                "target": self,
                "attr": "enc_plain",
                "default": DEFAULT_PLAINTEXT.replace("{cipher}", "ECC").replace(
                    "{actioned}", "encrypted"
                ),
            },
            {
                "kind": "button",
                "row": 2,
                "col": 0,
                "colspan": 3,
                "text": "Encrypt",
                "command": self._do_encrypt,
            },
            {"kind": "label", "row": 3, "col": 0, "text": "Encrypted data (hex):"},
            {
                "kind": "text",
                "row": 3,
                "col": 1,
                "colspan": 2,
                "target": self,
                "attr": "enc_ct",
                "readonly": True,
            },
        ]
        dec_config = [
            {"kind": "label", "row": 0, "col": 0, "text": "Your private key (PEM):"},
            {
                "kind": "text",
                "row": 0,
                "col": 1,
                "colspan": 2,
                "target": self,
                "attr": "dec_privkey",
            },
            {"kind": "label", "row": 1, "col": 0, "text": "Encrypted data (hex):"},
            {
                "kind": "text",
                "row": 1,
                "col": 1,
                "colspan": 2,
                "target": self,
                "attr": "dec_ct",
            },
            {
                "kind": "button",
                "row": 2,
                "col": 0,
                "colspan": 3,
                "text": "Decrypt",
                "command": self._do_decrypt,
            },
            {"kind": "label", "row": 3, "col": 0, "text": "Decrypted:"},
            {
                "kind": "text",
                "row": 3,
                "col": 1,
                "colspan": 2,
                "target": self,
                "attr": "dec_result",
                "readonly": True,
            },
        ]
        FormBuilder.build_multi_sections(
            self, [("Encrypt", enc_config), ("Decrypt", dec_config)]
        )

    def _do_encrypt(self):
        try:
            pub_pem = self.enc_pubkey.toPlainText().strip()
            plain = self.enc_plain.toPlainText()
            data = alg.encrypt(pub_pem, plain)
            getattr(self, "enc_ct_widget").setPlainText(encode_bytes_to_string(data))
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Encryption failed: {e}")

    def _do_decrypt(self):
        try:
            priv_pem = self.dec_privkey.toPlainText().strip()
            data = decode_string_to_bytes(self.dec_ct.toPlainText())
            pt = alg.decrypt(priv_pem, data)
            self.dec_result.setText(pt)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Decryption failed: {e}")
