from PySide6.QtWidgets import (QPushButton,QApplication,QToolTip,
                               QDialog,QVBoxLayout,QLineEdit,)
from PySide6.QtGui import QGuiApplication

class GMList(QDialog):
    def __init__(self,list_dict,parent=None):
        super().__init__(parent)
        self.setWindowTitle("Quick GM")
        layout = QVBoxLayout(self)
        for k,v in list_dict.items():
            if k == "重置宠物CD":
                button = QPushButton(f"{k}")
                
            if k == "Teleport":
                button = QPushButton(f"{k}")
                button.clicked.connect(lambda checked,
                                       t=v:self.show_input(t))
            else:
                button = QPushButton(f"{k}")
                button.clicked.connect(lambda checked,
                                    t=v:self.toclip(t))
            layout.addWidget(button)
        self.setLayout(layout)

    def toclip(self,text):
        cb = QGuiApplication.clipboard()
        cb.setText(text)

    def show_input(self,text):
        inDia = InputDia(text)
        if inDia.exec():
            inDia.show()
            return inDia
    
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



if __name__ == "__main__":
    app = QApplication()
    list = GMList(item_dict={})
    list.show()
    app.exec()