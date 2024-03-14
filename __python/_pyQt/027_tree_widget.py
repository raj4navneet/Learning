import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QFont, QPixmap, QIcon

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        self.tree = QTreeWidget()
        self.tree.setHeaderLabels(["xdf", "SDf", "sdf"])
        self.cmb = QComboBox()
        self.cmb.addItem("Item1", 'value1')
        self.cmb.addItem("Item2", 'value2')
        self.cmb.addItem("Item3", 'value3')

        #item = QTreeWidgetItem(self.tree)

        #self.tree.setItemWidget(item, 0 , self.cmb)
        cities =  QTreeWidgetItem(self.tree)
        cities.setText(0, "Cities")
        osloItem =  QTreeWidgetItem(cities)
        osloItem.setText(0, "Oslo")
        self.tree.setItemWidget(osloItem, 1, self.cmb)
        self.tree.setItemWidget(osloItem, 2, QLineEdit(self.tree))
        osloItem.setIcon(0, QIcon("d:\Icons\iOS 8 Icons\Png x72\Multitaks.png"))
        self.setCentralWidget(self.tree)
        

    def onMyToolBarButtonClick(self, s):
        print("click", s)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()