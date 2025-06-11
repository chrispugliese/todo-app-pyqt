import sys
from PyQt5.QtWidgets import (QApplication, 
                             QWidget, 
                             QVBoxLayout, 
                             QHBoxLayout, 
                             QLineEdit, 
                             QPushButton, 
                             QListWidget, 
                             QCheckBox, 
                             QDateEdit, 
                             QTimeEdit,
                             QMainWindow)
class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        widget = QCheckBox()
        widget.setCheckState(Qt.Checked)

        # For tristate: widget.setCheckState(Qt.PartiallyChecked)
        # Or: widget.setTriState(True)
        widget.stateChanged.connect(self.show_state)

        self.setCentralWidget(widget)

    def show_state(self, s):
        print(s == Qt.Checked)
        print(s)