import sys, random
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QVBoxLayout, QLabel, QMenu, QAction
from PyQt6.QtGui import QIcon, QKeySequence

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.show()
        self.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.customContextMenuRequested.connect(self.on_context_menu)

    def on_context_menu(self, pos):
        context = QMenu(self)
        context.addAction(QAction("test1", self))
        context.addAction(QAction("test2", self))
        context.addAction(QAction("test3", self))
        context.exec(self.mapToGlobal(pos))


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
