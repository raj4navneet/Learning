import sys
from PyQt5 import QtWidgets, QtCore

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.button_is_checked = True

        self.setWindowTitle("My App")

        button = QtWidgets.QPushButton("Press Me!")
        button.setCheckable(True)
        button.clicked.connect(self.button_toggled)
        button.setChecked(self.button_is_checked)

        self.setMinimumSize(QtCore.QSize(100, 100))
        self.setMaximumSize(QtCore.QSize(500, 500))

        self.setCentralWidget(button)

    def button_toggled(self, checked):
        print(self.button_is_checked)
        self.button_is_checked = checked

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()