from PyQt5.QtWidgets import QMessageBox, QVBoxLayout, QWidget

from app.encoding import (
    decode_string_to_bytes,
    encode_bytes_to_string,
)

from ....forms import FormBuilder
from ....helpers.key_derivation import DEFAULT_PASSPHRASE, DEFAULT_PLAINTEXT, derive_key
from . import alg

SEP = "§"


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
                "default": DEFAULT_PLAINTEXT.replace("{cipher}", "AES").replace(
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
            {"kind": "label", "row": 4, "col": 0, "text": "Nonce:"},
            {
                "kind": "entry",
                "row": 4,
                "col": 1,
                "colspan": 2,
                "target": self,
                "attr": "enc_nonce",
                "readonly": True,
            },
            {"kind": "label", "row": 5, "col": 0, "text": "Tag:"},
            {
                "kind": "entry",
                "row": 5,
                "col": 1,
                "colspan": 2,
                "target": self,
                "attr": "enc_tag",
                "readonly": True,
            },
            {"kind": "label", "row": 6, "col": 0, "text": "Ciphertext:"},
            {
                "kind": "entry",
                "row": 6,
                "col": 1,
                "colspan": 2,
                "target": self,
                "attr": "enc_ct",
                "readonly": True,
            },
            {"kind": "label", "row": 7, "col": 0, "text": "Combined:"},
            {
                "kind": "text",
                "row": 7,
                "col": 1,
                "colspan": 2,
                "target": self,
                "attr": "enc_combined",
                "readonly": True,
            },
        ]
        decrypt_config = [
            {
                "kind": "label",
                "row": 0,
                "col": 0,
                "text": "Paste combined data (nonce:tag:ct):",
            },
            {
                "kind": "text",
                "row": 0,
                "col": 1,
                "colspan": 2,
                "target": self,
                "attr": "dec_combined",
            },
            {"kind": "label", "row": 1, "col": 0, "text": "Nonce:"},
            {
                "kind": "entry",
                "row": 1,
                "col": 1,
                "colspan": 2,
                "target": self,
                "attr": "dec_nonce",
                "readonly": True,
            },
            {"kind": "label", "row": 2, "col": 0, "text": "Tag:"},
            {
                "kind": "entry",
                "row": 2,
                "col": 1,
                "colspan": 2,
                "target": self,
                "attr": "dec_tag",
                "readonly": True,
            },
            {"kind": "label", "row": 3, "col": 0, "text": "Ciphertext:"},
            {
                "kind": "text",
                "row": 3,
                "col": 1,
                "colspan": 2,
                "target": self,
                "attr": "dec_ct",
                "readonly": True,
            },
            {"kind": "label", "row": 4, "col": 0, "text": "Passphrase:"},
            {
                "kind": "entry",
                "row": 4,
                "col": 1,
                "colspan": 2,
                "target": self,
                "attr": "dec_pass",
            },
            {
                "kind": "button",
                "row": 5,
                "col": 0,
                "colspan": 3,
                "text": "Decrypt",
                "command": self._do_decrypt,
            },
            {"kind": "label", "row": 6, "col": 0, "text": "Decrypted:"},
            {
                "kind": "text",
                "row": 6,
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
            nonce, ct, tag = alg.encrypt(key, plain)

            self.enc_derived_key.setText(key.hex())
            self.enc_nonce.setText(encode_bytes_to_string(nonce))
            self.enc_tag.setText(encode_bytes_to_string(tag))
            self.enc_ct.setText(encode_bytes_to_string(ct))
            self.enc_combined.setPlainText(
                f"{encode_bytes_to_string(nonce)}{SEP}{encode_bytes_to_string(tag)}{SEP}{encode_bytes_to_string(ct)}"
            )
            self.dec_combined.setPlainText(
                f"{encode_bytes_to_string(nonce)}{SEP}{encode_bytes_to_string(tag)}{SEP}{encode_bytes_to_string(ct)}"
            )
            self.dec_pass.setText(self.enc_pass.text())

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Encryption failed: {e}")

    def _do_decrypt(self):
        try:
            raw = self.dec_combined.toPlainText().strip()
            if raw:
                parts = raw.split(SEP)
                self.dec_nonce.setText(parts[0])
                self.dec_tag.setText(parts[1])
                self.dec_ct.setPlainText(parts[2])

            key = derive_key(self.dec_pass.text(), 16)
            nonce = decode_string_to_bytes(self.dec_nonce.text())
            tag = decode_string_to_bytes(self.dec_tag.text())
            ct = decode_string_to_bytes(self.dec_ct.toPlainText())
            pt = alg.decrypt(key, nonce, ct, tag)
            self.dec_result.setText(pt)

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Decryption failed: {e}")
