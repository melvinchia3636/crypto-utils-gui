from PyQt5.QtWidgets import QMessageBox
from ....helpers.key_derivation import DEFAULT_PLAINTEXT
from ....helpers.content_tab import ContentTab
from ....helpers.form_builder import FormBuilder
from .. import alg


class SignVerifyTab(ContentTab):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._layout.setContentsMargins(16, 16, 16, 16)
        sign_config = [
            {"kind": "label", "row": 0, "col": 0, "text": "Private key (PEM):"},
            {
                "kind": "text",
                "row": 0,
                "col": 1,
                "colspan": 2,
                "target": self,
                "attr": "sign_privkey",
            },
            {"kind": "label", "row": 1, "col": 0, "text": "Message:"},
            {
                "kind": "text",
                "row": 1,
                "col": 1,
                "colspan": 2,
                "target": self,
                "attr": "sign_msg",
                "default": DEFAULT_PLAINTEXT.replace("{cipher}", "ECC").replace(
                    "{actioned}", "signed"
                ),
            },
            {
                "kind": "button",
                "row": 2,
                "col": 0,
                "colspan": 3,
                "text": "Sign",
                "command": self._do_sign,
            },
            {"kind": "label", "row": 3, "col": 0, "text": "Signature (hex):"},
            {
                "kind": "text",
                "row": 3,
                "col": 1,
                "colspan": 2,
                "target": self,
                "attr": "sign_sig",
                "readonly": True,
            },
        ]
        verify_config = [
            {"kind": "label", "row": 0, "col": 0, "text": "Signer public key (PEM):"},
            {
                "kind": "text",
                "row": 0,
                "col": 1,
                "colspan": 2,
                "target": self,
                "attr": "verify_pubkey",
            },
            {"kind": "label", "row": 1, "col": 0, "text": "Message:"},
            {
                "kind": "text",
                "row": 1,
                "col": 1,
                "colspan": 2,
                "target": self,
                "attr": "verify_msg",
            },
            {"kind": "label", "row": 2, "col": 0, "text": "Signature (hex):"},
            {
                "kind": "text",
                "row": 2,
                "col": 1,
                "colspan": 2,
                "target": self,
                "attr": "verify_sig",
            },
            {
                "kind": "button",
                "row": 3,
                "col": 0,
                "colspan": 3,
                "text": "Verify",
                "command": self._do_verify,
            },
            {"kind": "label", "row": 4, "col": 0, "text": "Result:"},
            {
                "kind": "entry",
                "row": 4,
                "col": 1,
                "colspan": 2,
                "target": self,
                "attr": "verify_result",
                "readonly": True,
            },
        ]
        FormBuilder.build_multi_sections(
            self, [("Sign", sign_config), ("Verify", verify_config)]
        )

    def _do_sign(self):
        try:
            priv_pem = self.sign_privkey.toPlainText().strip()
            msg = self.sign_msg.toPlainText()
            sig = alg.sign(priv_pem, msg)
            getattr(self, "sign_sig_widget").setPlainText(sig.hex())
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Signing failed: {e}")

    def _do_verify(self):
        try:
            pub_pem = self.verify_pubkey.toPlainText().strip()
            msg = self.verify_msg.toPlainText()
            sig = bytes.fromhex(self.verify_sig.toPlainText())
            ok = alg.verify(pub_pem, msg, sig)
            self.verify_result.setText(
                "Signature valid!" if ok else "Signature invalid!"
            )
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Verification failed: {e}")
