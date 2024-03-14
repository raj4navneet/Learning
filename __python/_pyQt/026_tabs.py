import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import *
class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        self.Tab = QTabWidget(self)
        self.Tab.setObjectName("Tab")

        self.Tab_1 = QWidget()
        self.Tab_1.setObjectName("Tab_1")
        self.Label_1 = QLabel(self.Tab_1)
        self.Label_1.setObjectName("Label_1")

        self.Tab_2 = QWidget()
        self.Tab_2.setObjectName("Tab_2")
        self.Label_2 = QLabel(self.Tab_2)
        self.Label_2.setObjectName("Label_2")

        self.Tab.addTab(self.Tab_1, " Tab 1")
        self.Tab.addTab(self.Tab_2, " Tab 2")
        self.Tab.setTabPosition(QTabWidget.East)
        self.Tab.setCurrentIndex(0)
        self.Tab.setTabShape(QTabWidget.Triangular)
        self.setCentralWidget(self.Tab)
        

    def onMyToolBarButtonClick(self, s):
        print("click", s)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()