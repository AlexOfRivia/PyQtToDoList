from PyQt6 import QtWidgets
from PyQt6.QtWidgets import *
import sys

#PRIORYTET ZADANIA
low = "Low"
medium = "Medium"
high = "ASAP!"

#initializing the window first
app = QApplication([])

win = QWidget()
win.setGeometry(650, 650, 800, 800)
win.setWindowTitle("To-Do List")
win.setStyleSheet("background-color: rgb(37, 37, 37);")

taskListWidget = QtWidgets.QListWidget()
taskListWidget.setStyleSheet("QListWidget { border-radius: 10px; background-color: rgb(230, 230, 230); " \
                             "padding: 10px; } QListWidget::item { border-radius:10px; background-color: rgb(200,200,200); padding: 10px; }")
taskListWidget.setSpacing(3)

taskCount = QtWidgets.QLabel()
taskCount.setText(f"Tasks: {taskListWidget.count()}")

mainlayout = QtWidgets.QVBoxLayout() #main app layout
topBarLayout = QtWidgets.QHBoxLayout() #top bar layout

#task input field
titleInput = QtWidgets.QLineEdit()
titleInput.setStyleSheet("max-height: 40px;")
titleInput.setPlaceholderText("Enter task title")
topBarLayout.addWidget(titleInput)
titleInput.setStyleSheet("QLineEdit { border-radius: 10px; max-height: 40px; padding: 5px; " \
                             "background-color: rgb(230, 230, 230); }")
#task priority combobox
priorityInput = QtWidgets.QComboBox()
priorityInput.addItems([low, medium, high]) #these are the priorities I made earlier
topBarLayout.addWidget(priorityInput)
priorityInput.setStyleSheet("QComboBox {"
                            "border-radius: 10px;"
                            "max-height: 40px;"
                            "padding: 5px;"
                            "background-color: rgb(230, 230, 230);"
                            "border: 1px solid #c4c4c4;"
                            "color: black;"
                            "}"
                            "QComboBox::drop-down {"
                            "subcontrol-origin: padding;"
                            "subcontrol-position: top right;"
                            "width: 20px;"
                            "border-left-width: 1px;"
                            "border-left-color: #c4c4c4;"
                            "border-left-style: solid;"
                            "border-top-right-radius: 9px;"
                            "border-bottom-right-radius: 9px;"
                            "}"
                            "QComboBox QAbstractItemView {"
                            "border: 1px solid #c4c4c4;"
                            "border-radius: 10px;"
                            "background-color: rgb(230, 230, 230);"
                            "selection-background-color: rgb(119,221,119);"
                            "padding: 5px;"
                            "}"
                            )

#button for adding tasks into the list
addTaskButton = QtWidgets.QPushButton("Add Task")
addTaskButton.setStyleSheet("QPushButton { border-radius: 10px; max-height: 40px; " \
                            "background-color: rgb(119,221,119); color: white; border: " \
                            "none; padding: 5px 10px; } QPushButton:hover { background-color: rgb(105,198,105); } " \
                            "QPushButton:pressed { background-color: rgb(90,175,90); }")

def addTask():
    taskTitle = titleInput.text().strip()
    taskPriority = priorityInput.currentText()

    if taskTitle:  #only adding if there's something written
        taskItem = f"{taskTitle} - Priority: {taskPriority}"
        taskListWidget.addItem(taskItem)
        titleInput.clear()  #clear input field after adding
        taskCount.setText(f"Tasks: {taskListWidget.count()}")
    else:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Warning)
        msg.setText("Task title field cannot be empty!")
        msg.setWindowTitle("Warning")
        msg.exec()



#button for deleting selected task from the list
deleteTaskButton = QtWidgets.QPushButton("Delete Selected Task")
deleteTaskButton.setStyleSheet("QPushButton { border-radius: 10px; max-height: 40px; " \
                            "background-color: rgb(255,99,71); color: white; border: " \
                            "none; padding: 5px 10px; } QPushButton:hover { background-color: rgb(235,79,51); } " \
                            "QPushButton:pressed { background-color: rgb(215,59,31); }")
def delTask():
    selectedItem = taskListWidget.currentRow()
    if selectedItem >=0:
        taskListWidget.takeItem(selectedItem)
        taskCount.setText(f"Tasks: {taskListWidget.count()}")
    else:
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
        msg.setText("No task selected to delete!")
        msg.setWindowTitle("Warning")
        msg.exec()
deleteTaskButton.clicked.connect(delTask)
addTaskButton.clicked.connect(addTask)

bottomLayout = QHBoxLayout()


topBarLayout.addWidget(deleteTaskButton)
topBarLayout.addWidget(addTaskButton)

mainlayout.addItem(topBarLayout)
mainlayout.addWidget(taskListWidget)

win.setLayout(mainlayout)

#executing the app etc
win.show()
sys.exit(app.exec())


