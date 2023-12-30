import sys
from PyQt5 import QtWidgets, QtCore

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.button_is_checked = True

        self.setWindowTitle("My App")

        self.button = QtWidgets.QPushButton("Press Me!")
        self.button.setCheckable(True)
        self.button.pressed.connect(self.button_pressed)
        self.button.released.connect(self.button_released)
        self.button.setChecked(self.button_is_checked)

        self.setMinimumSize(QtCore.QSize(100, 100))
        self.setMaximumSize(QtCore.QSize(500, 500))

        self.setCentralWidget(self.button)

    def button_pressed(self):
        print("FIRE!!!")

    def button_released(self):
        print("RELOAD!!")

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()