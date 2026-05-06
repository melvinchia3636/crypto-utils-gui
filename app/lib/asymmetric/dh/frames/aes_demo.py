from PyQt5.QtWidgets import QMessageBox
from .....helpers.key_derivation import DEFAULT_PLAINTEXT
from .....helpers.content_tab import ContentTab
from .....helpers.form_builder import FormBuilder
from .. import alg


SEP = ":"


class AesGcmDemoTab(ContentTab):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._layout.setContentsMargins(16, 16, 16, 16)

        alice_side = [
            {"kind": "label", "row": 1, "col": 0, "text": "Alice's private key (PEM):"},
            {
                "kind": "text",
                "row": 1,
                "col": 1,
                "colspan": 2,
                "target": self,
                "attr": "alice_enc_priv",
            },
            {"kind": "label", "row": 2, "col": 0, "text": "Bob's public key (PEM):"},
            {
                "kind": "text",
                "row": 2,
                "col": 1,
                "colspan": 2,
                "target": self,
                "attr": "alice_enc_peer",
            },
            {"kind": "label", "row": 3, "col": 0, "text": "Derived shared key (hex):"},
            {
                "kind": "text",
                "row": 3,
                "col": 1,
                "colspan": 2,
                "target": self,
                "attr": "alice_shared_key",
                "readonly": True,
            },
            {"kind": "label", "row": 4, "col": 0, "text": "Plaintext:"},
            {
                "kind": "text",
                "row": 4,
                "col": 1,
                "colspan": 2,
                "target": self,
                "attr": "aes_plain",
                "default": DEFAULT_PLAINTEXT.replace(
                    "{cipher}", "DH + AES-GCM"
                ).replace("{actioned}", "encrypted"),
            },
            {
                "kind": "button",
                "row": 5,
                "col": 0,
                "colspan": 3,
                "text": "Encrypt for Bob",
                "command": self._do_encrypt,
            },
            {
                "kind": "label",
                "row": 6,
                "col": 0,
                "text": "Combined (nonce:tag:ct hex):",
            },
            {
                "kind": "text",
                "row": 6,
                "col": 1,
                "colspan": 2,
                "target": self,
                "attr": "aes_combined",
                "readonly": True,
            },
        ]
        bob_side = [
            {"kind": "label", "row": 1, "col": 0, "text": "Bob's private key (PEM):"},
            {
                "kind": "text",
                "row": 1,
                "col": 1,
                "colspan": 2,
                "target": self,
                "attr": "bob_dec_priv",
            },
            {"kind": "label", "row": 2, "col": 0, "text": "Alice's public key (PEM):"},
            {
                "kind": "text",
                "row": 2,
                "col": 1,
                "colspan": 2,
                "target": self,
                "attr": "bob_dec_peer",
            },
            {"kind": "label", "row": 3, "col": 0, "text": "Derived shared key (hex):"},
            {
                "kind": "text",
                "row": 3,
                "col": 1,
                "colspan": 2,
                "target": self,
                "attr": "bob_shared_key",
                "readonly": True,
            },
            {
                "kind": "label",
                "row": 4,
                "col": 0,
                "text": "Combined (nonce:tag:ct hex):",
            },
            {
                "kind": "text",
                "row": 4,
                "col": 1,
                "colspan": 2,
                "target": self,
                "attr": "bob_dec_combined",
            },
            {
                "kind": "button",
                "row": 5,
                "col": 0,
                "colspan": 3,
                "text": "Decrypt from Alice",
                "command": self._do_decrypt,
            },
            {"kind": "label", "row": 6, "col": 0, "text": "Decrypted:"},
            {
                "kind": "entry",
                "row": 6,
                "col": 1,
                "colspan": 2,
                "target": self,
                "attr": "aes_result",
                "readonly": True,
            },
        ]
        FormBuilder.build_multi_sections(
            self, [("Alice Encrypts", alice_side), ("Bob Decrypts", bob_side)]
        )

    def _do_encrypt(self):
        try:
            alice_priv = alg.import_priv_key(self.alice_enc_priv.toPlainText().strip())
            bob_pub = alg.import_pub_key(self.alice_enc_peer.toPlainText().strip())
            _, derived = alg.compute_shared_secret(alice_priv, bob_pub)
            getattr(self, "alice_shared_key_widget").setPlainText(derived.hex())
            plain = self.aes_plain.toPlainText()
            nonce, ct, tag = alg.aes_gcm_encrypt(derived, plain)
            combined = f"{nonce.hex()}{SEP}{tag.hex()}{SEP}{ct.hex()}"
            self.aes_combined.setPlainText(combined)
            self.bob_dec_combined.setPlainText(combined)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Encryption failed: {e}")

    def _do_decrypt(self):
        try:
            bob_priv = alg.import_priv_key(self.bob_dec_priv.toPlainText().strip())
            alice_pub = alg.import_pub_key(self.bob_dec_peer.toPlainText().strip())
            _, derived = alg.compute_shared_secret(bob_priv, alice_pub)
            getattr(self, "bob_shared_key_widget").setPlainText(derived.hex())
            raw = self.bob_dec_combined.toPlainText().strip()
            parts = raw.split(SEP)
            nonce = bytes.fromhex(parts[0])
            tag = bytes.fromhex(parts[1])
            ct = bytes.fromhex(parts[2])
            pt = alg.aes_gcm_decrypt(derived, nonce, ct, tag)
            self.aes_result.setText(pt)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Decryption failed: {e}")
