from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QGridLayout
from PyQt5 import  QtGui, QtCore
from PyQt5.QtGui import QPixmap
from  base_frame import BaseFrame

class EndGame(BaseFrame):
    def __init__(self, score):
        super(EndGame, self).__init__()
        self.score = score
        self.setFixedWidth(500)
        self.addLabels()
        self.addLogo()

    def addLabels(self):
        print(self.score)
        title = QLabel("YOU WIN THE GAME,\n you Score:", self)
        title.setAlignment(QtCore.Qt.AlignLeft)
        title.setStyleSheet(
            "font-family: Shanti;" +
            "font-size: 25px;" +
            "color: 'white';" +
            "padding: 75px;"
            )
        title.setWordWrap(True);
        self.layout().addWidget(title, 0, 0)

        score = QLabel(str(self.score), self)
        score.setAlignment(QtCore.Qt.AlignCenter)
        score.setStyleSheet(
            "font-size: 48px;" +
            "font-family: Shanti;" +
            "color: 'white';"
        )
        self.layout().addWidget(score, 0, 1)

    def addLogo(self):
        image = "logo_bottom.png"
        try:
            with open(image):
                logo = QLabel(self)
                logo_image = QPixmap(image)
                logo.setPixmap(logo_image)
                logo.setAlignment(QtCore.Qt.AlignCenter)
                logo.setStyleSheet("margin-top: 75px; margin-bottom: 30px;")
                # First parameter is the Widget followed by the row and the column
                self.layout().addWidget(logo, 4, 0, 1, 2)
        except FileNotFoundError:
            print("Image not found")