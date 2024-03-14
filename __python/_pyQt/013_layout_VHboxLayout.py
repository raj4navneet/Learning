import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget
from customLayoutWidget_Color import Color

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()

    self.setWindowTitle("My App")

    layout = QHBoxLayout()

    layout.addWidget(Color("red"))
    layout.addWidget(Color("blue"))
    layout.addWidget(Color("green"))
    layout.addWidget(Color("yellow"))

    widget = QWidget()
    widget.setLayout(layout)
    self.setCentralWidget(widget)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()