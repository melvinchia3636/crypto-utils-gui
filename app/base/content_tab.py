from PyQt5.QtWidgets import QGridLayout, QTabWidget, QVBoxLayout, QWidget


class ContentTab(QWidget):
    def __init__(self, parent=None, use_grid=False):
        super().__init__(parent)
        self._parent_frame = parent
        self._layout = QVBoxLayout(self)
        self._grid = None
        if use_grid:
            self._grid = QGridLayout()
            self._layout.addLayout(self._grid)

    def set_layout_margins(self, left, top, right, bottom):
        self._layout.setContentsMargins(left, top, right, bottom)


class TabbedFrame(QWidget):
    tab_specs = []

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setLayout(QVBoxLayout(self))
        tabs = QTabWidget()
        for tab_class, title in self.tab_specs:
            instance = tab_class(self)
            tabs.addTab(instance, title)
        self._tabs = tabs
        self.layout().addWidget(tabs)
