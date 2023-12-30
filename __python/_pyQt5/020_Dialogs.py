import sys
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QPushButton, QDialog, QDialogButtonBox, QMessageBox
from PyQt5.QtGui import QIcon, QKeySequence


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        button  = QPushButton("Press me for Dialog")
        button.clicked.connect(self.button_clicked)
        button.setCheckable(True)
        self.setCentralWidget(button)
        

    def button_clicked(self, s):
        print("click", s)
        dlg = QMessageBox(self)
        dlg.setWindowTitle("I have a question")
        dlg.setText("SIMPLE DIALOG")
        dlg.setStandardButtons(QMessageBox.StandardButton.No | QMessageBox.StandardButton.Yes)
        dlg.setIcon(QMessageBox.Icon.Question)
        button1 = dlg.exec()

        button = QMessageBox.StandardButton(button1)

        if button == QMessageBox.StandardButton.Yes:
            print("It's a Yes")
        elif button == QMessageBox.StandardButton.No:
            print("It's a No")
        else:
            print("WHHHAAT")


class CustomDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Dialog 1 !")

        QBtn = QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel
        
        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        message = QLabel(" Something Happened, is that OK ?")
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

foo = app.exec()
print(foo)
print(foo)