import first_script
import second_script
import third_script
import iterator

from PyQt5.QtGui import QFont
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel


import sys
import os


def application():
    app = QApplication(sys.argv)
    window = Window()
    window.setFixedSize (800, 600)
    window.setObjectName("MainWindow")
    window.setStyleSheet(
        "#MainWindow{border-image:url(phon.jpg)}")
    window.show()
    sys.exit(app.exec_())
if __name__ == "__main__":
    application()