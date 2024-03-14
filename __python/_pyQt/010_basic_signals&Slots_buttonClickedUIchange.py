import sys
from PyQt6 import QtWidgets, QtCore
from random import choice
window_titles = [
  'My App',
  'My App',
  'Still My App',
  'Still My App',
  'What on earth',
  'What on earth',
  'This is surprising',
  'This is surprising',
  'Something went wrong'
]

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("MY APP")
        
        self.label = QtWidgets.QLabel()

        self.input = QtWidgets.QLineEdit()
        self.input.textChanged.connect(self.setWindowTitle)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.label)

        container = QtWidgets.QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()