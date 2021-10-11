from PyQt5.QtWidgets import  QLabel, QPushButton, QGridLayout
from PyQt5.QtGui import QPixmap
from PyQt5 import  QtCore
from PyQt5.QtGui import QCursor
from base_frame import BaseFrame
from trivia_game import TriviaGame

class MainWindow(BaseFrame):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.addLogo()
        self.addButton()

    def addLogo(self):
        image = "logo.png"
        try:
            with open(image):
                logo = QLabel(self)
                logo_image = QPixmap(image)
                logo.setPixmap(logo_image)
                logo.setAlignment(QtCore.Qt.AlignCenter)
                logo.setStyleSheet("margin-top: 100px;")
                #First parameter is the Widget followed by the row and the column
                self.layout().addWidget(logo, 0, 0)
        except FileNotFoundError:
            print("Image not found")

    def addButton(self):
        button = QPushButton("PLAY",self)
        button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        button.setStyleSheet(
            "*{border: 4px solid '#BC006C';" +
            "border-radius: 45px;" +
            "font-size: 35px;" +
            "color: 'white';" +
            "padding: 25px 0;" +
            "margin: 100px 200px;}" +
            "*:hover{ background: '#BC006C'; }"
        )
        button.clicked.connect(self.show_second_form)
        self.layout().addWidget(button, 1,0)

    def show_second_form(self):
        self.child_win = TriviaGame()
        self.child_win.show()
        self.hide()