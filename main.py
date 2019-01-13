import sys


#from view.login import Login
from PyQt5.QtWidgets import QApplication

from view.window import Window
if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())