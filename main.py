import sys
from user_interface import Form
from PySide6.QtWidgets import QApplication

if __name__ == "__main__":
    app = QApplication()
    form = Form()
    form.show()
    sys.exit(app.exec())