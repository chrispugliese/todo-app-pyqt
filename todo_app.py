import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (QApplication, 
                             QWidget,
                             QLabel, 
                             QVBoxLayout, 
                             QHBoxLayout, 
                             QLineEdit, 
                             QPushButton, 
                             QListWidget, 
                             QCheckBox, 
                             QDateEdit, 
                             QTimeEdit)

class ToDoApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("To-Do List")
        self.setGeometry(200, 200, 1000, 800)

        self.tasks = []
        self.completed_tasks = []
        
        self.layout = QVBoxLayout()

        self.title_label = QLabel("Type in a task below!")
        self.title_label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)


        self.input_field = QLineEdit()
        self.add_button = QPushButton("Add Task")

        self.task_label = QLabel("Things to do.")
        self.task_label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.task_list = QListWidget()

        self.completed_task_label = QLabel("Tasks you've completed. If you want to delete a task, select the task, then press delete button.")
        self.completed_task_label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.complete_task_list = QListWidget()


        self.layout.addWidget(self.title_label)
        self.layout.addWidget(self.input_field)
        self.layout.addWidget(self.add_button)
        self.layout.addWidget(self.task_label)
        self.layout.addWidget(self.task_list)
        self.layout.addWidget(self.completed_task_label)
        self.layout.addWidget(self.complete_task_list)

        # add buttton
        self.add_button.clicked.connect(self.add_task)

        # press enter to add task
        self.input_field.returnPressed.connect(self.add_task)

        #delete button
        self.delete_button = QPushButton("Delete Task")
        self.delete_button.clicked.connect(self.delete_task)
        self.layout.addWidget(self.delete_button)
        
        #complete button    
        self.mark_complete_button = QPushButton("Mark Complete")
        self.mark_complete_button.clicked.connect(self.mark_complete)
        self.layout.addWidget(self.mark_complete_button)



        self.setLayout(self.layout)

    def add_task(self):
        task = self.input_field.text()
        if task:
            self.tasks.append(task)
            self.task_list.addItem(task)
            self.input_field.clear()

    def delete_task(self):

        # deleting initial tasks
        selected_items = self.task_list.selectedItems()
        if selected_items:
            for item in selected_items:
                self.task_list.takeItem(self.task_list.row(item))

        # deleting completed tasks
        selected_complete_items = self.complete_task_list.selectedItems()
        if selected_complete_items: 
            for item in selected_complete_items:
                self.complete_task_list.takeItem(self.complete_task_list.row(item))
    
    def mark_complete(self):
        selected_items = self.task_list.selectedItems()
        for item in selected_items:
            self.complete_task_list.addItem(item.text())
            self.task_list.takeItem(self.task_list.row(item))






if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ToDoApp()
    window.show()
    sys.exit(app.exec_())