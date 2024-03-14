import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        button = QPushButton("Press Me!")
        self.setMinimumSize(QSize(100, 100))
        self.setMaximumSize(QSize(500, 500))
        # Set the central widget of the Window.
        self.setCentralWidget(button)
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()