from PyQt5.QtWidgets import QGridLayout, QMessageBox, QVBoxLayout, QWidget

from ...forms import FormBuilder
from ...helpers.format_utils import ETA_LEGEND, format_eta, format_speed
from ..lib.dictionary import AesDictionaryWorker, DesDictionaryWorker


CIPHERS = [
    ("DES", "iv§ct"),
    ("AES-128-GCM", "nonce§tag§ct"),
]


class DictionaryTab(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(16, 16, 16, 16)

        gl = QGridLayout()
        layout.addLayout(gl)
        config = [
            {"kind": "label", "row": 0, "col": 0, "text": "Cipher:"},
            {
                "kind": "combobox",
                "row": 0,
                "col": 1,
                "colspan": 2,
                "target": self,
                "attr": "cipher",
                "items": [c[0] for c in CIPHERS],
                "default": "DES",
            },
            {"kind": "label", "row": 1, "col": 0, "text": "Combined data:"},
            {
                "kind": "text",
                "row": 1,
                "col": 1,
                "colspan": 2,
                "target": self,
                "attr": "enc_combined",
                "max_height": 60,
            },
            {"kind": "label", "row": 2, "col": 0, "text": "Known plaintext:"},
            {
                "kind": "text",
                "row": 2,
                "col": 1,
                "colspan": 2,
                "target": self,
                "attr": "known_text",
                "max_height": 60,
                "default": "Hello",
            },
            {"kind": "label", "row": 3, "col": 0, "text": "Wordlist file:"},
            {
                "kind": "file",
                "row": 3,
                "col": 1,
                "colspan": 2,
                "target": self,
                "attr": "wordlist_path",
            },
            {
                "kind": "button",
                "row": 4,
                "col": 0,
                "colspan": 2,
                "text": "Start",
                "command": self._do_attack,
                "target": self,
                "attr": "start_btn",
            },
            {
                "kind": "button",
                "row": 4,
                "col": 2,
                "text": "Cancel",
                "command": self._cancel,
                "target": self,
                "attr": "cancel_btn",
            },
            {
                "kind": "progressbar",
                "row": 5,
                "col": 0,
                "colspan": 3,
                "target": self,
                "attr": "progress",
            },
            {"kind": "label", "row": 6, "col": 0, "text": "Found passphrase:"},
            {
                "kind": "entry",
                "row": 6,
                "col": 1,
                "colspan": 2,
                "target": self,
                "attr": "found_pass",
                "readonly": True,
            },
            {"kind": "label", "row": 7, "col": 0, "text": "Derived key (hex):"},
            {
                "kind": "entry",
                "row": 7,
                "col": 1,
                "colspan": 2,
                "target": self,
                "attr": "found_key",
                "readonly": True,
            },
            {"kind": "label", "row": 8, "col": 0, "text": "Decrypted:"},
            {
                "kind": "text",
                "row": 8,
                "col": 1,
                "colspan": 2,
                "target": self,
                "attr": "decrypted",
                "readonly": True,
                "max_height": 60,
            },
            {"kind": "note", "row": 9, "col": 0, "colspan": 3, "text": ETA_LEGEND},
        ]
        FormBuilder.build_single_section(gl, config)

        layout.addStretch()

        self._worker = None
        self.cancel_btn.setEnabled(False)

    def _do_attack(self):
        raw = self.enc_combined.toPlainText().strip()
        if "§" not in raw:
            QMessageBox.critical(self, "Error", "Combined data must use § separator")
            return

        wl_path = self.wordlist_path.text().strip()
        if not wl_path:
            QMessageBox.critical(self, "Error", "Please select a wordlist file")
            return

        parts = raw.split("§")
        known = self.known_text.toPlainText().strip()

        self.progress.setValue(0)
        self.progress.setFormat("%p% (%v keys)")
        self.progress_label.setText("")
        self.found_pass.setText("")
        self.found_key.setText("")
        self.decrypted.setPlainText("")
        self.start_btn.setEnabled(False)
        self.cancel_btn.setEnabled(True)

        cipher_name = self.cipher_combo.currentText()
        if cipher_name == "DES":
            self._worker = DesDictionaryWorker(
                bytes.fromhex(parts[0]), bytes.fromhex(parts[1]), known, wl_path
            )
        else:
            self._worker = AesDictionaryWorker(
                bytes.fromhex(parts[0]),
                bytes.fromhex(parts[1]),
                bytes.fromhex(parts[2]),
                known,
                wl_path,
            )

        self._worker.progress.connect(self._on_progress)
        self._worker.found.connect(self._on_found)
        self._worker.not_found.connect(self._on_not_found)
        self._worker.start()

    def _cancel(self):
        if self._worker:
            self._worker.cancel()
        self.start_btn.setEnabled(True)
        self.cancel_btn.setEnabled(False)

    def _on_progress(self, current, total, elapsed):
        if total > 0:
            self.progress.setMaximum(total)
            self.progress.setValue(current)
        else:
            self.progress.setMaximum(0)
            self.progress.setValue(0)

        if elapsed > 0.01 and current > 0:
            speed = current / elapsed
            remaining = total - current if total > 0 else 0
            eta = remaining / speed if remaining > 0 else 0
            self.progress_label.setText(
                f"Speed: {format_speed(speed)}  |  ETA: {format_eta(eta)}"
            )

    def _on_found(self, key, text):
        self.found_key.setText(key.hex())
        self.decrypted.setPlainText(text)
        self.start_btn.setEnabled(True)
        self.cancel_btn.setEnabled(False)
        QMessageBox.information(
            self, "Key Found!", f"Key (hex): {key.hex()}\nDecrypted: {text}"
        )

    def _on_not_found(self):
        self.start_btn.setEnabled(True)
        self.cancel_btn.setEnabled(False)
        QMessageBox.information(self, "Result", "Passphrase not found in wordlist")
