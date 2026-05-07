from PyQt5.QtWidgets import QApplication


class Encoder:
    name = ""
    _example = b"Hello"
    group = ""

    def encode(self, data: bytes) -> str:
        raise NotImplementedError

    def decode(self, text: str) -> bytes:
        raise NotImplementedError

    def get_example(self) -> str:
        return self.encode(self._example)

    @staticmethod
    def current() -> str:
        for w in QApplication.topLevelWidgets():
            if hasattr(w, "encoding_selector"):
                text = w.encoding_selector.combo.currentText().strip()

                return text.split(" (")[0] if " (" in text else text

        return "Hex"
