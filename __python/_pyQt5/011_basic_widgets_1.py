import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtGui import QPixmap, QMovie

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()

    self.setWindowTitle("My App")

    widget = QLabel("Hello")
    font = widget.font()
    font.setPointSize(30)
    widget.setFont(font)
    widget.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter) 

    widget1 = QLabel("Hello")
    movie = QPixmap("D:\Images\Art\Screenshot 2022-02-19 142529.png")
    widget1.setPixmap(movie)
    widget.setScaledContents(True)
    widget1.setScaledContents(True)
    
    layout = QVBoxLayout()
    layout.addWidget(widget)
    layout.addWidget(widget1)

    container = QWidget()
    container.setLayout(layout)

    self.setCentralWidget(container)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()