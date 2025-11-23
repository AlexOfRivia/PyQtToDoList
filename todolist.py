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
win.setGeometry(400, 400, 800, 800)
win.setWindowTitle("To-Do List")

taskListWidget = QtWidgets.QListWidget()
taskCount = QtWidgets.QLabel()
taskCount.setText(f"Tasks: {taskListWidget.count()}")

mainlayout = QtWidgets.QVBoxLayout() #main app layout
topBarLayout = QtWidgets.QHBoxLayout() #top bar layout

#task input field
titleInput = QtWidgets.QLineEdit()
titleInput.setStyleSheet("max-height: 40px;")
titleInput.setPlaceholderText("Enter task title")
topBarLayout.addWidget(titleInput)

#task priority combobox
priorityInput = QtWidgets.QComboBox()
priorityInput.addItems([low, medium, high]) #these are the priorities I made earlier
topBarLayout.addWidget(priorityInput)

#button for adding tasks into the list
addTaskButton = QtWidgets.QPushButton("Add Task")
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
topBarLayout.addWidget(deleteTaskButton)


addTaskButton.clicked.connect(addTask)
topBarLayout.addWidget(addTaskButton)


mainlayout.addItem(topBarLayout)
mainlayout.addWidget(taskListWidget)

win.setLayout(mainlayout)

#executing the app etc
win.show()
sys.exit(app.exec())


