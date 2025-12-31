from PySide6.QtWidgets import (QPushButton,QToolTip,
                               QDialog,QVBoxLayout,QLineEdit,)
from PySide6.QtGui import QGuiApplication

class InputDia(QDialog):
    def __init__(self,text,title,parent=None):
        super().__init__(parent)
        self.creat_subwidgets(text,title)

    def creat_subwidgets(self,text,title):
        self.edit = QLineEdit(self,placeholderText="Enter text here")
        self.button = QPushButton("Confirm")
        if title == "重置宠物CD" or title == "觉醒单个宠物":
            self.button.setToolTip()

        self.button.clicked.connect(lambda checked,
                                    t=text:self.toclip(t))
        layout = QVBoxLayout(self)
        layout.addWidget(self.edit)
        layout.addWidget(self.button)
        self.button.clicked.connect(self.reject)


    def toclip(self,text):
        cb = QGuiApplication.clipboard()
        cb.setText(f"{text}({self.edit.text()})")