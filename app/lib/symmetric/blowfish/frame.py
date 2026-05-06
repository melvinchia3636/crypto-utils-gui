from PyQt5.QtWidgets import QWidget, QVBoxLayout, QMessageBox
from ....helpers.form_builder import FormBuilder
from ....helpers.key_derivation import derive_key, DEFAULT_PASSPHRASE, DEFAULT_PLAINTEXT
from . import alg

SEP = ":"


class Frame(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setLayout(QVBoxLayout(self))

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
                "default": DEFAULT_PLAINTEXT.replace("{cipher}", "Blowfish").replace(
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
            {"kind": "label", "row": 3, "col": 0, "text": "Derived key (hex):"},
            {
                "kind": "entry",
                "row": 3,
                "col": 1,
                "colspan": 2,
                "target": self,
                "attr": "enc_derived_key",
                "readonly": True,
            },
            {"kind": "label", "row": 4, "col": 0, "text": "IV (hex):"},
            {
                "kind": "entry",
                "row": 4,
                "col": 1,
                "colspan": 2,
                "target": self,
                "attr": "enc_iv",
                "readonly": True,
            },
            {"kind": "label", "row": 5, "col": 0, "text": "Ciphertext (hex):"},
            {
                "kind": "entry",
                "row": 5,
                "col": 1,
                "colspan": 2,
                "target": self,
                "attr": "enc_ct",
                "readonly": True,
            },
            {"kind": "label", "row": 6, "col": 0, "text": "Combined:"},
            {
                "kind": "text",
                "row": 6,
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
                "text": "Paste combined data (iv:ct):",
            },
            {
                "kind": "text",
                "row": 0,
                "col": 1,
                "colspan": 2,
                "target": self,
                "attr": "dec_combined",
            },
            {"kind": "label", "row": 1, "col": 0, "text": "IV (hex):"},
            {
                "kind": "entry",
                "row": 1,
                "col": 1,
                "colspan": 2,
                "target": self,
                "attr": "dec_iv",
                "readonly": True,
            },
            {"kind": "label", "row": 2, "col": 0, "text": "Ciphertext (hex):"},
            {
                "kind": "text",
                "row": 2,
                "col": 1,
                "colspan": 2,
                "target": self,
                "attr": "dec_ct",
                "readonly": True,
            },
            {"kind": "label", "row": 3, "col": 0, "text": "Passphrase:"},
            {
                "kind": "entry",
                "row": 3,
                "col": 1,
                "colspan": 2,
                "target": self,
                "attr": "dec_pass",
            },
            {
                "kind": "button",
                "row": 4,
                "col": 0,
                "colspan": 3,
                "text": "Decrypt",
                "command": self._do_decrypt,
            },
            {"kind": "label", "row": 5, "col": 0, "text": "Decrypted:"},
            {
                "kind": "text",
                "row": 5,
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
            iv, ct = alg.encrypt(key, plain)
            self.enc_derived_key.setText(key.hex())
            self.enc_iv.setText(iv.hex())
            self.enc_ct.setText(ct.hex())
            self.enc_combined.setPlainText(f"{iv.hex()}{SEP}{ct.hex()}")
            self.dec_combined.setPlainText(f"{iv.hex()}{SEP}{ct.hex()}")
            self.dec_pass.setText(self.enc_pass.text())
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Encryption failed: {e}")

    def _do_decrypt(self):
        try:
            raw = self.dec_combined.toPlainText().strip()
            if raw:
                parts = raw.split(SEP)
                self.dec_iv.setText(parts[0])
                self.dec_ct.setPlainText(parts[1])
            key = derive_key(self.dec_pass.text(), 16)
            iv = bytes.fromhex(self.dec_iv.text())
            ct = bytes.fromhex(self.dec_ct.toPlainText())
            pt = alg.decrypt(key, iv, ct)
            self.dec_result.setText(pt)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Decryption failed: {e}")
