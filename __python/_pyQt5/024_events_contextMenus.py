import sys, random
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QVBoxLayout, QLabel, QMenu, QAction
from PyQt5.QtGui import QIcon, QKeySequence

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = QLabel("Click in this Window")
        self.setMouseTracking(True)
        self.setCentralWidget(self.label)


    def contextMenuEvent(self, e):
        context = QMenu(self)
        context.addAction(QAction("test1", self))
        context.addAction(QAction("test2", self))
        context.addAction(QAction("test3", self))
        context.exec(e.globalPos())


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
