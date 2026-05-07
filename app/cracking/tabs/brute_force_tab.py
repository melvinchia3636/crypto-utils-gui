from PyQt5.QtWidgets import QGridLayout, QMessageBox, QVBoxLayout, QWidget

from ...forms import FormBuilder
from ..lib.aes_brute_force import AesBruteForceWorker
from ..lib.des_brute_force import DesBruteForceWorker
from ...helpers.format_utils import ETA_LEGEND, format_eta, format_speed


CIPHERS = [
    ("DES", "iv§ct", 8, "0000000000000000"),
    ("AES-128-GCM", "nonce§tag§ct", 16, "00000000000000000000000000000000"),
]


class BruteForceTab(QWidget):
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
            {"kind": "label", "row": 3, "col": 0, "text": "Key start (hex):"},
            {
                "kind": "entry",
                "row": 3,
                "col": 1,
                "target": self,
                "attr": "key_start",
                "default": "0000000000000000",
            },
            {
                "kind": "entry",
                "row": 3,
                "col": 2,
                "target": self,
                "attr": "key_end",
                "default": "00000000000000FF",
            },
            {
                "kind": "button",
                "row": 4,
                "col": 0,
                "colspan": 2,
                "text": "Start Brute Force",
                "command": self._do_brute_force,
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
            {"kind": "label", "row": 6, "col": 0, "text": "Found key (hex):"},
            {
                "kind": "entry",
                "row": 6,
                "col": 1,
                "colspan": 2,
                "target": self,
                "attr": "found_key",
                "readonly": True,
            },
            {"kind": "label", "row": 7, "col": 0, "text": "Decrypted:"},
            {
                "kind": "text",
                "row": 7,
                "col": 1,
                "colspan": 2,
                "target": self,
                "attr": "decrypted",
                "readonly": True,
                "max_height": 60,
            },
            {"kind": "note", "row": 8, "col": 0, "colspan": 3, "text": ETA_LEGEND},
        ]
        FormBuilder.build_single_section(gl, config)

        layout.addStretch()

        self._worker = None
        self.cancel_btn.setEnabled(False)
        self.cipher_combo.currentIndexChanged.connect(self._on_cipher_changed)
        self._on_cipher_changed()

    def _on_cipher_changed(self):
        fmt, size = CIPHERS[self.cipher_combo.currentIndex()][1:3]
        self.key_start.setText("0" * (size * 2))
        self.key_end.setText("0" * (size * 2 - 2) + "FF")

    def _do_brute_force(self):
        raw = self.enc_combined.toPlainText().strip()
        if "§" not in raw:
            QMessageBox.critical(self, "Error", "Combined data must use § separator")
            return

        parts = raw.split("§")
        known = self.known_text.toPlainText().strip()
        start = int(self.key_start.text().strip(), 16)
        end = int(self.key_end.text().strip(), 16)

        self.progress.setValue(0)
        self.progress.setFormat("%p% (%v/%m keys)")
        self.progress_label.setText("")
        self.found_key.setText("")
        self.decrypted.setPlainText("")
        self.start_btn.setEnabled(False)
        self.cancel_btn.setEnabled(True)

        cipher_name = self.cipher_combo.currentText()
        if cipher_name == "DES":
            self._worker = DesBruteForceWorker(
                bytes.fromhex(parts[0]), bytes.fromhex(parts[1]), known, start, end
            )
        else:
            self._worker = AesBruteForceWorker(
                bytes.fromhex(parts[0]),
                bytes.fromhex(parts[1]),
                bytes.fromhex(parts[2]),
                known,
                start,
                end,
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
            self.progress.setValue(int(current / total * 100))
        if elapsed > 0.01 and current > 0:
            speed = current / elapsed
            self.progress_label.setText(
                f"Speed: {format_speed(speed)}  |  ETA: {format_eta((total - current) / speed)}"
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
        QMessageBox.information(self, "Result", "Key not found in the specified range")
