import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QGridLayout, QStackedLayout
from customLayoutWidget_Color import Color

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()

    self.setWindowTitle("My App")

    layout1 = QStackedLayout()

    layout1.addWidget(Color("red"))
    layout1.addWidget(Color("blue"))
    layout1.addWidget(Color("green"))
    layout1.addWidget(Color("yellow"))
    layout1.setCurrentIndex(2)

    widget = QWidget()
    widget.setLayout(layout1)
    self.setCentralWidget(widget)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()