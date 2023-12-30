import sys, random
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QPushButton, QDialog, QDialogButtonBox, QMessageBox
from PyQt5.QtGui import QIcon, QKeySequence

class anotherWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Another Window " + str(random.randint(0, 100)))
        self.anotherLabel = QLabel("WASSUP")
        self.setCentralWidget(self.anotherLabel)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Main Window")

        self.w = anotherWindow()
        self.newWinBTN = QPushButton("Press for a new Window")
        self.newWinBTN.clicked.connect(self.toggleWindow)
        self.setCentralWidget(self.newWinBTN)
    
    def toggleWindow(self, checked):
        if self.w.isVisible():
            self.w.hide()
        else:
            self.w.show()


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
