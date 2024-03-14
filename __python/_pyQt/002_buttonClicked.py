import sys
from PyQt6 import QtWidgets, QtCore

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        button = QtWidgets.QPushButton("Press Me!")
        button.setCheckable(True)
        button.clicked.connect(self.button_clicked)
        button.clicked.connect(self.button_toggled)

        self.setMinimumSize(QtCore.QSize(100, 100))
        self.setMaximumSize(QtCore.QSize(500, 500))

        self.setCentralWidget(button)
    
    def button_clicked(self):
        print("OLLLLLLLLA!!")

    def button_toggled(self, rtf):
        print("Checked?", rtf)

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()