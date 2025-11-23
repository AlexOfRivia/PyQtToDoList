from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

#PRIORYTET ZADANIA
low = "Low"
medium = "Medium"
high = "ASAP!"

#initializing the window first
app = QApplication(sys.argv)

win = QMainWindow()
win.setGeometry(400, 400, 800, 800)
win.setWindowTitle("To-Do List")




#executing the app etc
win.show()
sys.exit(app.exec_())


