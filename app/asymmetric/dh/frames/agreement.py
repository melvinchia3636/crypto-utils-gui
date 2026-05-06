from PyQt5.QtWidgets import QMessageBox
from ....helpers.content_tab import ContentTab
from ....helpers.form_builder import FormBuilder
from .. import alg


class AgreementTab(ContentTab):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._layout.setContentsMargins(16, 16, 16, 16)

        alice_config = [
            {"kind": "label", "row": 1, "col": 0, "text": "Private key (PEM):"},
            {
                "kind": "text",
                "row": 1,
                "col": 1,
                "colspan": 2,
                "target": self,
                "attr": "alice_priv",
            },
            {"kind": "label", "row": 2, "col": 0, "text": "Peer's public key (PEM):"},
            {
                "kind": "text",
                "row": 2,
                "col": 1,
                "colspan": 2,
                "target": self,
                "attr": "alice_peer_pub",
            },
        ]
        bob_config = [
            {"kind": "label", "row": 1, "col": 0, "text": "Private key (PEM):"},
            {
                "kind": "text",
                "row": 1,
                "col": 1,
                "colspan": 2,
                "target": self,
                "attr": "bob_priv",
            },
            {"kind": "label", "row": 2, "col": 0, "text": "Peer's public key (PEM):"},
            {
                "kind": "text",
                "row": 2,
                "col": 1,
                "colspan": 2,
                "target": self,
                "attr": "bob_peer_pub",
            },
        ]
        compute_config = [
            {
                "kind": "button",
                "row": 0,
                "col": 0,
                "colspan": 3,
                "text": "Compute Shared Secrets",
                "command": self._do_compute,
            },
            {"kind": "label", "row": 1, "col": 0, "text": "Status:"},
            {
                "kind": "entry",
                "row": 1,
                "col": 1,
                "colspan": 2,
                "target": self,
                "attr": "compute_status",
                "readonly": True,
            },
            {"kind": "label", "row": 2, "col": 0, "text": "Raw shared secret (hex):"},
            {
                "kind": "text",
                "row": 2,
                "col": 1,
                "colspan": 2,
                "target": self,
                "attr": "raw_secret",
                "readonly": True,
            },
            {"kind": "label", "row": 3, "col": 0, "text": "HKDF-derived (hex):"},
            {
                "kind": "text",
                "row": 3,
                "col": 1,
                "colspan": 2,
                "target": self,
                "attr": "derived_secret",
                "readonly": True,
            },
        ]
        FormBuilder.build_multi_sections(
            self,
            [("Alice", alice_config), ("Bob", bob_config), ("Compute", compute_config)],
        )

    def _do_compute(self):
        try:
            alice_priv = alg.import_priv_key(self.alice_priv.toPlainText().strip())
            alice_peer_pub = alg.import_pub_key(
                self.alice_peer_pub.toPlainText().strip()
            )
            bob_priv = alg.import_priv_key(self.bob_priv.toPlainText().strip())
            bob_peer_pub = alg.import_pub_key(self.bob_peer_pub.toPlainText().strip())

            alice_raw, alice_derived = alg.compute_shared_secret(
                alice_priv, alice_peer_pub
            )
            bob_raw, bob_derived = alg.compute_shared_secret(bob_priv, bob_peer_pub)

            if alice_raw == bob_raw and alice_derived == bob_derived:
                self.compute_status.setText("Valid")
                getattr(self, "raw_secret_widget").setPlainText(alice_raw.hex())
                getattr(self, "derived_secret_widget").setPlainText(alice_derived.hex())
            else:
                self.compute_status.setText("Invalid - secrets do not match")
                getattr(self, "raw_secret_widget").setPlainText("")
                getattr(self, "derived_secret_widget").setPlainText("")
        except Exception as e:
            self.compute_status.setText("Error")
            getattr(self, "raw_secret_widget").setPlainText("")
            getattr(self, "derived_secret_widget").setPlainText("")
