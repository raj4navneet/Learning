import sys
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QToolBar, QAction, QStatusBar, QFileIconProvider
from PyQt6.QtGui import QIcon


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        label = QLabel("Hello!")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.setCentralWidget(label)
        
        toolbar = QToolBar("My main toolbar")
        toolbar.setIconSize(QSize(50, 50))
        self.addToolBar(toolbar)
        
        button_action = QAction(QIcon("D:\Icons\iOS 8 Icons\Png x72\Photo Booth.png"), "Your button", self)
        button_action.setStatusTip("This is your button")
        button_action.triggered.connect(self.onMyToolBarButtonClick)
        button_action.setCheckable(True)
        toolbar.addAction(button_action)

        button_action1 = QAction(QIcon("D:\Icons\iOS 8 Icons\Png x72\Podcats.png"), "Your button", self)
        button_action1.setStatusTip("This is your 2nd button")
        button_action1.triggered.connect(self.onMyToolBarButtonClick)
        button_action1.setCheckable(True)
        toolbar.addAction(button_action1)

        self.setStatusBar(QStatusBar(self))

    def onMyToolBarButtonClick(self, s):
        print("click", s)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()