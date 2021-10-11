from PyQt5.QtWidgets import QWidget, QGridLayout

class BaseFrame(QWidget):
    def __init__(self):
        super(BaseFrame, self).__init__()
        self.setWindowTitle("Who Wants to be a programmer???")
        self.setFixedWidth(1000)
        self.setStyleSheet("background: #161219;")
        self.setLayout(QGridLayout())



