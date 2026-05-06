from PyQt5.QtWidgets import QMessageBox

from app.encoding import (
    decode_string_to_bytes,
    encode_bytes_to_string,
)

from .....base.content_tab import ContentTab
from .....forms import FormBuilder
from .....helpers.key_derivation import DEFAULT_PLAINTEXT
from .. import alg


class EncryptDecryptTab(ContentTab):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._layout.setContentsMargins(16, 16, 16, 16)
        enc_config = [
            {"kind": "label", "row": 0, "col": 0, "text": "Public key (PEM):"},
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
                "default": DEFAULT_PLAINTEXT.replace(
                    "{cipher}", "RSA (PKCS1_OAEP)"
                ).replace("{actioned}", "encrypted"),
            },
            {
                "kind": "button",
                "row": 2,
                "col": 0,
                "colspan": 3,
                "text": "Encrypt",
                "command": self._do_encrypt,
            },
            {"kind": "label", "row": 3, "col": 0, "text": "Ciphertext (hex):"},
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
            {"kind": "label", "row": 0, "col": 0, "text": "Private key (PEM):"},
            {
                "kind": "text",
                "row": 0,
                "col": 1,
                "colspan": 2,
                "target": self,
                "attr": "dec_privkey",
            },
            {"kind": "label", "row": 1, "col": 0, "text": "Passphrase (optional):"},
            {
                "kind": "entry",
                "row": 1,
                "col": 1,
                "colspan": 2,
                "target": self,
                "attr": "dec_pass",
            },
            {"kind": "label", "row": 2, "col": 0, "text": "Ciphertext (hex):"},
            {
                "kind": "text",
                "row": 2,
                "col": 1,
                "colspan": 2,
                "target": self,
                "attr": "dec_ct",
            },
            {
                "kind": "button",
                "row": 3,
                "col": 0,
                "colspan": 3,
                "text": "Decrypt",
                "command": self._do_decrypt,
            },
            {"kind": "label", "row": 4, "col": 0, "text": "Decrypted:"},
            {
                "kind": "text",
                "row": 4,
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
            ct = alg.encrypt(pub_pem, plain)
            getattr(self, "enc_ct_widget").setPlainText(encode_bytes_to_string(ct))
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Encryption failed: {e}")

    def _do_decrypt(self):
        try:
            priv_pem = self.dec_privkey.toPlainText().strip()
            passphrase = self.dec_pass.text().strip() or None
            ct = decode_string_to_bytes(self.dec_ct.toPlainText())
            pt = alg.decrypt(priv_pem, ct, passphrase)
            self.dec_result.setText(pt)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Decryption failed: {e}")
