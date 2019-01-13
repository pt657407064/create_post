import sys
from PyQt5 import QtGui

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QPlainTextEdit, QLineEdit, QMessageBox
from controller.create_post import create_post


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "Create Post"
        self.top = 100
        self.left = 100
        self.width = 680
        self.height = 1000

        # Title Area
        self.line = QLineEdit(self)
        self.line.move(50, 50)
        self.line.resize(575, 30)

        # Text Area
        self.text_area = QPlainTextEdit(self)
        self.text_area.move(50, 100)
        self.text_area.resize(575, 500)

        # Button UI
        self.submit_btn = QPushButton("发帖", self)
        self.submit_btn.move(300, 850)
        self.submit_btn.clicked.connect(self.click_btn)

        # Msg Box
        self.msg = QMessageBox()
        self.msg.setTextFormat(Qt.RichText)

        self.InitWindow()

    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setFixedSize(self.width, self.height)
        self.show()

    def click_btn(self):
        self.submit_btn.setDisabled(True)
        title_text = self.line.text()
        post_text = self.text_area.toPlainText()
        is_success, val = create_post(title_text, post_text)
        if is_success:
            self.msg.setText(str(val))
            self.msg.setWindowTitle("成功")
            self.msg.exec()
            self.text_area.setPlainText("")
            self.line.setText("")
        else:
            self.msg.warning(self, "失败", str(val))
        self.submit_btn.setDisabled(False)
