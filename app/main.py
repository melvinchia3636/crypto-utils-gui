from PyQt5.QtWidgets import QApplication, QTabWidget, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QComboBox
from .lib.symmetric.symmetric_frame import SymmetricWidget
from .lib.asymmetric.asymmetric_frame import AsymmetricWidget
import sys


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Crypto Utility Tool")
        self.resize(1000, 700)

        layout = QVBoxLayout(self)
        top_bar = QHBoxLayout()
        top_bar.addWidget(QLabel("Encoding:"))
        self.encoding_combo = QComboBox()
        self.encoding_combo.addItems(["hex", "base64", "base32", "base16"])
        self.encoding_combo.setCurrentText("hex")
        top_bar.addWidget(self.encoding_combo, 1)
        layout.addLayout(top_bar)
        tabs = QTabWidget()
        tabs.addTab(SymmetricWidget(), "Symmetric")
        tabs.addTab(AsymmetricWidget(), "Asymmetric")
        layout.addWidget(tabs)


def main():
    app = QApplication(sys.argv)
    w = App()
    w.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
