from PyQt5.QtWidgets import QApplication, QTabWidget, QWidget, QVBoxLayout
from app.symmetric.symmetric_frame import SymmetricWidget
from app.asymmetric.asymmetric_frame import AsymmetricWidget
import sys


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Crypto Utility Tool")
        self.resize(1000, 700)

        layout = QVBoxLayout(self)
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
