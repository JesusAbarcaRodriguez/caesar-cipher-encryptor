from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow
class MainView(QMainWindow):
    def __init__(self):  # this
        super(MainView, self).__init__()
        uic.loadUi("view/view.ui", self)
