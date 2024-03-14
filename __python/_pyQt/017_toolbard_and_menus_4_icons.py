import sys
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QToolBar, QAction, QStatusBar, QCheckBox
from PyQt6.QtGui import QIcon


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        label = QLabel("Hello!")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.setCentralWidget(label)
        
        #Creating ToolBar
        toolbar = QToolBar("My main toolbar")
        toolbar.setIconSize(QSize(32, 32))
        toolbar.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.addToolBar(toolbar)
        
        #Creating 1st Action
        button_action = QAction(QIcon("D:\Icons\iOS 8 Icons\Png x72\Photo Booth.png"), "Button 1", self)
        button_action.setStatusTip("This is your butto 1n")
        button_action.triggered.connect(self.onMyToolBarButtonClick)
        button_action.setCheckable(True)

        #Creating 2nd Action
        button_action1 = QAction(QIcon("D:\Icons\iOS 8 Icons\Png x72\Podcats.png"), "Button 2", self)
        button_action1.setStatusTip("This is your 2nd button")
        button_action1.triggered.connect(self.onMyToolBarButtonClick)
        button_action1.setCheckable(True)

        #Layouting the ToolBar
        toolbar.addAction(button_action)
        toolbar.addAction(button_action1)
        toolbar.addSeparator()
        toolbar.addWidget(QLabel(" MUHAHAH !! "))
        toolbar.addSeparator()
        toolbar.addWidget(QCheckBox())

        self.setStatusBar(QStatusBar(self))

    def onMyToolBarButtonClick(self, s):
        print("click", s)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()