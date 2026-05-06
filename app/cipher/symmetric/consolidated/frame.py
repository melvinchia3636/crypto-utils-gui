from PyQt5.QtWidgets import QGridLayout, QMessageBox, QVBoxLayout, QWidget

from app.encoding import (
    encode_bytes_to_string,
)

from ....forms import FormBuilder
from ....helpers.key_derivation import DEFAULT_PASSPHRASE, DEFAULT_PLAINTEXT, derive_key
from .. import aes, blowfish, des, des3, rc4, twofish

SEP = "§"


class Frame(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)
        layout.setContentsMargins(16, 16, 16, 16)
        gl = QGridLayout()
        layout.addLayout(gl)
        config = [
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
                "default": DEFAULT_PLAINTEXT.replace(
                    "{cipher}", "Consolidated"
                ).replace("{actioned}", "encrypted"),
            },
            {
                "kind": "button",
                "row": 2,
                "col": 0,
                "colspan": 3,
                "text": "Encrypt with All",
                "command": self._do_encrypt_all,
            },
            {"kind": "label", "row": 3, "col": 0, "text": "DES:"},
            {
                "kind": "text",
                "row": 3,
                "col": 1,
                "colspan": 2,
                "target": self,
                "attr": "des_ct",
                "readonly": True,
            },
            {"kind": "label", "row": 4, "col": 0, "text": "3DES:"},
            {
                "kind": "text",
                "row": 4,
                "col": 1,
                "colspan": 2,
                "target": self,
                "attr": "des3_ct",
                "readonly": True,
            },
            {"kind": "label", "row": 5, "col": 0, "text": "AES:"},
            {
                "kind": "text",
                "row": 5,
                "col": 1,
                "colspan": 2,
                "target": self,
                "attr": "aes_ct",
                "readonly": True,
            },
            {"kind": "label", "row": 6, "col": 0, "text": "Blowfish:"},
            {
                "kind": "text",
                "row": 6,
                "col": 1,
                "colspan": 2,
                "target": self,
                "attr": "blowfish_ct",
                "readonly": True,
            },
            {"kind": "label", "row": 7, "col": 0, "text": "Twofish:"},
            {
                "kind": "text",
                "row": 7,
                "col": 1,
                "colspan": 2,
                "target": self,
                "attr": "twofish_ct",
                "readonly": True,
            },
            {"kind": "label", "row": 8, "col": 0, "text": "RC4:"},
            {
                "kind": "text",
                "row": 8,
                "col": 1,
                "colspan": 2,
                "target": self,
                "attr": "rc4_ct",
                "readonly": True,
            },
        ]
        FormBuilder.build_single_section(gl, config)
        layout.addStretch()

    def _do_encrypt_all(self):
        try:
            passphrase = self.enc_pass.text()
            plaintext = self.enc_plain.toPlainText()

            des_key = derive_key(passphrase, 8)
            iv, ct = des.alg.encrypt(des_key, plaintext)
            self.des_ct.setPlainText(
                f"{encode_bytes_to_string(iv)}{SEP}{encode_bytes_to_string(ct)}"
            )

            des3_key = derive_key(passphrase, 24)
            iv, ct = des3.alg.encrypt(des3_key, plaintext)
            self.des3_ct.setPlainText(
                f"{encode_bytes_to_string(iv)}{SEP}{encode_bytes_to_string(ct)}"
            )

            aes_key = derive_key(passphrase, 16)
            nonce, ct, tag = aes.alg.encrypt(aes_key, plaintext)
            self.aes_ct.setPlainText(
                f"{encode_bytes_to_string(nonce)}{SEP}{encode_bytes_to_string(tag)}{SEP}{encode_bytes_to_string(ct)}"
            )

            bf_key = derive_key(passphrase, 16)
            iv, ct = blowfish.alg.encrypt(bf_key, plaintext)
            self.blowfish_ct.setPlainText(
                f"{encode_bytes_to_string(iv)}{SEP}{encode_bytes_to_string(ct)}"
            )

            tf_key = derive_key(passphrase, 16)
            ct_hex = twofish.alg.encrypt(tf_key, plaintext)
            self.twofish_ct.setPlainText(encode_bytes_to_string(bytes.fromhex(ct_hex)))

            rc4_key = derive_key(passphrase, 16)
            ct_bytes = rc4.alg.encrypt(rc4_key, plaintext)
            self.rc4_ct.setPlainText(encode_bytes_to_string(ct_bytes))
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Encryption failed: {e}")
