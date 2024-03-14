import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QPixmap, QMovie

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        widget = QLineEdit()
        widget.setMaxLength(10)
        widget.setPlaceholderText("Enter your text")
        # widget.setReadOnly(True) # uncomment this to make readonly
        widget.returnPressed.connect(self.return_pressed)
        widget.selectionChanged.connect(self.selection_changed)
        widget.textChanged.connect(self.text_changed)
        widget.textEdited.connect(self.text_edited)
        widget.setInputMask("+00-000-000-0000")
        self.setCentralWidget(widget)

    def return_pressed(self):
        print("Return pressed!")
        self.centralWidget().setText("BOOM!")

    def selection_changed(self):
        print("Selection changed")
        print(self.centralWidget().selectedText())

    def text_changed(self, s):
        print("Text changed...")
        print(s)
    def text_edited(self, s):
        print("Text edited...")
        print(s)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()