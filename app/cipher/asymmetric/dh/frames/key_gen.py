from PyQt5.QtWidgets import QMessageBox
from .....helpers.content_tab import ContentTab
from .....helpers.form_builder import FormBuilder
from .. import alg


class KeyGenTab(ContentTab):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._layout.setContentsMargins(16, 16, 16, 16)

        params_config = [
            {"kind": "label", "row": 0, "col": 0, "text": "Parameters (PEM):"},
            {
                "kind": "text",
                "row": 0,
                "col": 1,
                "colspan": 2,
                "target": self,
                "attr": "kg_params",
            },
            {
                "kind": "button",
                "row": 1,
                "col": 0,
                "colspan": 3,
                "text": "Generate Both Key Pairs",
                "command": self._do_keygen,
            },
        ]
        alice_config = [
            {"kind": "label", "row": 0, "col": 0, "text": "Alice's public key:"},
            {
                "kind": "text",
                "row": 0,
                "col": 1,
                "colspan": 2,
                "target": self,
                "attr": "alice_pub",
                "readonly": True,
            },
            {"kind": "label", "row": 1, "col": 0, "text": "Alice's private key:"},
            {
                "kind": "text",
                "row": 1,
                "col": 1,
                "colspan": 2,
                "target": self,
                "attr": "alice_priv",
                "readonly": True,
            },
        ]
        bob_config = [
            {"kind": "label", "row": 0, "col": 0, "text": "Bob's public key:"},
            {
                "kind": "text",
                "row": 0,
                "col": 1,
                "colspan": 2,
                "target": self,
                "attr": "bob_pub",
                "readonly": True,
            },
            {"kind": "label", "row": 1, "col": 0, "text": "Bob's private key:"},
            {
                "kind": "text",
                "row": 1,
                "col": 1,
                "colspan": 2,
                "target": self,
                "attr": "bob_priv",
                "readonly": True,
            },
        ]
        FormBuilder.build_multi_sections(
            self,
            [
                ("Parameters", params_config),
                ("Alice", alice_config),
                ("Bob", bob_config),
            ],
        )

    def _do_keygen(self):
        try:
            params_pem = self.kg_params.toPlainText().strip()
            params = alg.params_from_pem(params_pem)
            alice_priv = params.generate_private_key()
            alice_pub = alice_priv.public_key()
            bob_priv = params.generate_private_key()
            bob_pub = bob_priv.public_key()
            getattr(self, "alice_pub_widget").setPlainText(
                alg.export_pub_key(alice_pub)
            )
            getattr(self, "alice_priv_widget").setPlainText(
                alg.export_priv_key(alice_priv)
            )
            getattr(self, "bob_pub_widget").setPlainText(alg.export_pub_key(bob_pub))
            getattr(self, "bob_priv_widget").setPlainText(alg.export_priv_key(bob_priv))
            agree_tab = self._parent_frame._tabs.widget(2)
            agree_tab.alice_priv.setPlainText(alg.export_priv_key(alice_priv))
            agree_tab.alice_peer_pub.setPlainText(alg.export_pub_key(bob_pub))
            agree_tab.bob_priv.setPlainText(alg.export_priv_key(bob_priv))
            agree_tab.bob_peer_pub.setPlainText(alg.export_pub_key(alice_pub))
            aes_tab = self._parent_frame._tabs.widget(3)
            aes_tab.alice_enc_priv.setPlainText(alg.export_priv_key(alice_priv))
            aes_tab.alice_enc_peer.setPlainText(alg.export_pub_key(bob_pub))
            aes_tab.bob_dec_priv.setPlainText(alg.export_priv_key(bob_priv))
            aes_tab.bob_dec_peer.setPlainText(alg.export_pub_key(alice_pub))
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Key generation failed: {e}")
