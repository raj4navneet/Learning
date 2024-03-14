import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QGridLayout, QStackedLayout
from customLayoutWidget_Color import Color

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()

    self.setWindowTitle("My App")

    layout1 = QGridLayout()

    layout1.addWidget(Color("red"), 0, 0)
    layout1.addWidget(Color("blue"), 1, 1)
    layout1.addWidget(Color("green"), 1, 2)
    layout1.addWidget(Color("yellow"), 0, 1)

    widget = QWidget()
    widget.setLayout(layout1)
    self.setCentralWidget(widget)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()