import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget
from customLayoutWidget_Color import Color

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()

    self.setWindowTitle("My App")

    layout1 = QHBoxLayout()
    layout2 = QVBoxLayout()
    layout3 = QVBoxLayout()

    layout2.addWidget(Color("red"))
    layout2.addWidget(Color("blue"))
    layout2.addWidget(Color("green"))
    layout2.addWidget(Color("yellow"))

    layout1.addLayout(layout2)
    layout1.addWidget(Color("purple"))
    layout1.setContentsMargins(0, 0, 0, 0)
    layout1.setSpacing(4)

    layout3.addWidget(Color("teal"))
    layout3.addWidget(Color("orange"))
    layout3.addWidget(Color("indigo"))

    layout1.addLayout(layout3)

    widget = QWidget()
    widget.setLayout(layout1)
    self.setCentralWidget(widget)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()