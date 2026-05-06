from PyQt5.QtWidgets import QMessageBox, QVBoxLayout, QWidget

from app.encoding import (
    decode_string_to_bytes,
    encode_bytes_to_string,
)

from ....forms import FormBuilder
from ....helpers.key_derivation import DEFAULT_PASSPHRASE, DEFAULT_PLAINTEXT, derive_key
from . import alg


class Frame(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setLayout(QVBoxLayout(self))
        self.layout().setContentsMargins(0, 0, 0, 0)

        encrypt_config = [
            {"kind": "label", "row": 0, "col": 0, "text": "Passphrase:"},
            {
                "kind": "entry",
                "row": 0,
                "col": 1,
                "colspan": 2,
                "target": self,
                "attr": "enc_pass",
                "default": DEFAULT_PASSPHRASE,
            },
            {"kind": "label", "row": 1, "col": 0, "text": "Plaintext:"},
            {
                "kind": "text",
                "row": 1,
                "col": 1,
                "colspan": 2,
                "target": self,
                "attr": "enc_plain",
                "default": DEFAULT_PLAINTEXT.replace("{cipher}", "RC4").replace(
                    "{actioned}", "encoded"
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
            {"kind": "label", "row": 3, "col": 0, "text": "Derived key:"},
            {
                "kind": "entry",
                "row": 3,
                "col": 1,
                "colspan": 2,
                "target": self,
                "attr": "enc_derived_key",
                "readonly": True,
            },
            {"kind": "label", "row": 4, "col": 0, "text": "Ciphertext:"},
            {
                "kind": "entry",
                "row": 4,
                "col": 1,
                "colspan": 2,
                "target": self,
                "attr": "enc_ct",
                "readonly": True,
            },
        ]
        decrypt_config = [
            {"kind": "label", "row": 0, "col": 0, "text": "Passphrase:"},
            {
                "kind": "entry",
                "row": 0,
                "col": 1,
                "colspan": 2,
                "target": self,
                "attr": "dec_pass",
            },
            {"kind": "label", "row": 1, "col": 0, "text": "Ciphertext:"},
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
            self, [("Encryption", encrypt_config), ("Decryption", decrypt_config)]
        )

    def _do_encrypt(self):
        try:
            key = derive_key(self.enc_pass.text(), 16)
            plain = self.enc_plain.toPlainText()
            ct = alg.encrypt(key, plain)
            self.enc_derived_key.setText(key.hex())
            self.enc_ct.setText(encode_bytes_to_string(ct))
            self.dec_ct.setPlainText(encode_bytes_to_string(ct))
            self.dec_pass.setText(self.enc_pass.text())

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Encryption failed: {e}")

    def _do_decrypt(self):
        try:
            key = derive_key(self.dec_pass.text(), 16)
            ct = decode_string_to_bytes(self.dec_ct.toPlainText())
            pt = alg.decrypt(key, ct)
            self.dec_result.setText(pt)

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Decryption failed: {e}")
