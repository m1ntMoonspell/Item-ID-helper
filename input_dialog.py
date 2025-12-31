from PySide6.QtWidgets import (QPushButton,QApplication,QToolTip,
                               QDialog,QVBoxLayout,QLineEdit,)
from PySide6.QtGui import QGuiApplication

class InputDia(QDialog):
    def __init__(self,text,parent=None):
        super().__init__(parent)
        self.edit = QLineEdit(self,placeholderText="Enter text here")
        self.button = QPushButton("Confirm")
        self.button.clicked.connect(lambda checked,
                                    t=text:self.toclip(t))
        layout = QVBoxLayout(self)
        layout.addWidget(self.edit)
        layout.addWidget(self.button)
        self.button.clicked.connect(self.reject)

    def toclip(self,text):
        cb = QGuiApplication.clipboard()
        cb.setText(f"{text}({self.edit.text()})")