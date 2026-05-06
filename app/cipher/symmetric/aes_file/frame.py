import os
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QMessageBox
from Crypto.Random import get_random_bytes
from ....forms import FormBuilder
from . import alg


class Frame(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setLayout(QVBoxLayout(self))

        encrypt_config = [
            {"kind": "label", "row": 0, "col": 0, "text": "Source file:"},
            {
                "kind": "file",
                "row": 0,
                "col": 1,
                "colspan": 2,
                "target": self,
                "attr": "enc_src",
                "dialog_title": "Select file",
            },
            {
                "kind": "label",
                "row": 1,
                "col": 0,
                "text": "Key (16 bytes, hex, or leave empty to generate):",
            },
            {
                "kind": "entry",
                "row": 1,
                "col": 1,
                "colspan": 2,
                "target": self,
                "attr": "enc_key",
            },
            {
                "kind": "button",
                "row": 2,
                "col": 0,
                "colspan": 3,
                "text": "Encrypt File",
                "command": self._do_encrypt,
            },
        ]
        decrypt_config = [
            {"kind": "label", "row": 0, "col": 0, "text": "Encrypted file:"},
            {
                "kind": "file",
                "row": 0,
                "col": 1,
                "colspan": 2,
                "target": self,
                "attr": "dec_src",
                "dialog_title": "Select file",
            },
            {"kind": "label", "row": 1, "col": 0, "text": "Key (16 bytes, hex):"},
            {
                "kind": "entry",
                "row": 1,
                "col": 1,
                "colspan": 2,
                "target": self,
                "attr": "dec_key",
            },
            {
                "kind": "button",
                "row": 2,
                "col": 0,
                "colspan": 3,
                "text": "Decrypt File",
                "command": self._do_decrypt,
            },
        ]
        FormBuilder.build_multi_sections(
            self, [("Encrypt File", encrypt_config), ("Decrypt File", decrypt_config)]
        )

    def _do_encrypt(self):
        try:
            src = self.enc_src.text()
            if not src:
                QMessageBox.critical(self, "Error", "Please select a source file.")
                return
            base, ext = os.path.splitext(src)
            dst = f"{base}_encrypted{ext}"
            key_str = self.enc_key.text().strip()
            if key_str:
                key = bytes.fromhex(key_str)
                if len(key) != 16:
                    raise ValueError
            else:
                key = get_random_bytes(16)
                self.enc_key.setText(key.hex())
            with open(src, "rb") as f:
                data = f.read()
            nonce, ct, tag = alg.encrypt(key, data)
            with open(dst, "wb") as f:
                f.write(nonce)
                f.write(tag)
                f.write(ct)
            QMessageBox.information(
                self, "Success", f"Encrypted -> {dst}\nKey: {key.hex()}"
            )
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Encryption failed: {e}")

    def _do_decrypt(self):
        try:
            src = self.dec_src.text()
            if not src:
                QMessageBox.critical(self, "Error", "Please select an encrypted file.")
                return
            base, ext = os.path.splitext(src)
            if base.endswith("_encrypted"):
                base = base[:-10]
            dst = f"{base}_decrypted{ext}"
            key_str = self.dec_key.text().strip()
            if not key_str:
                QMessageBox.critical(self, "Error", "Please enter the key.")
                return
            key = bytes.fromhex(key_str)
            if len(key) != 16:
                raise ValueError
            with open(src, "rb") as f:
                nonce = f.read(12)
                tag = f.read(16)
                ct = f.read()
            data = alg.decrypt(key, nonce, ct, tag)
            with open(dst, "wb") as f:
                f.write(data)
            QMessageBox.information(self, "Success", f"Decrypted -> {dst}")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Decryption failed: {e}")
