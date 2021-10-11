from PyQt5.QtWidgets import QApplication, QLabel, QPushButton,QWidget, QFileDialog, QGridLayout
from PyQt5.QtGui import QPixmap
from PyQt5 import  QtGui, QtCore

from urllib.request import urlopen
import json
import pandas as pd
import random

import loose_frame
import win_frame
from base_frame import BaseFrame

parameters= \
    {
        "question" : [],
        "answer1": [],
        "answer2": [],
        "answer3": [],
        "answer4": [],
        "correct": []
    }

def preload_data(idx):
    with urlopen("https://opentdb.com/api.php?amount=50&category=18&difficulty=medium&type=multiple") as webpage:
        data = json.loads(webpage.read().decode())
        df = pd.DataFrame(data["results"])

        question_data = df["question"][idx]
        correct = df["correct_answer"][idx]
        wrong_answers = df["incorrect_answers"][idx]

        formatting = [
            ("#039;", "'"),
            ("&;", "'"),
            ("&quot;", '"'),
            ("&lt;", "<"),
            ("&gt;", ">")
        ]

        # Formatting text
        for tuple in formatting:
            question_data = question_data.replace(tuple[0], tuple[1])
            correct = correct.replace(tuple[0], tuple[1])

        for tuple in formatting:
            wrong_answers = [char.replace(tuple[0], tuple[1]) for char in wrong_answers]

        parameters["question"].append(question_data)
        parameters["correct"].append(correct)
        parameters["correct"].append(correct)

        all_answers = wrong_answers + [correct]  # Convert correct to list
        random.shuffle(all_answers)
        parameters["answer1"].append(all_answers[0])
        parameters["answer2"].append(all_answers[1])
        parameters["answer3"].append(all_answers[2])
        parameters["answer4"].append(all_answers[3])
        print(parameters)




class TriviaGame(BaseFrame):
    def __init__(self):
        super(TriviaGame, self).__init__()
        preload_data(random.randint(0, 49))
        self.score = 0
        self.score_label = QLabel(str(self.score), self)
        self.addLabels()
        self.addButton()
        self.addLogo()

    def addLogo(self):
        image = "logo_bottom.png"
        try:
            with open(image):
                logo = QLabel(self)
                logo_image = QPixmap(image)
                logo.setPixmap(logo_image)
                logo.setAlignment(QtCore.Qt.AlignCenter)
                logo.setStyleSheet("margin-top: 75px; margin-bottom: 30px;")
                #First parameter is the Widget followed by the row and the column
                self.layout().addWidget(logo, 4, 0, 1, 2)
        except FileNotFoundError:
            print("Image not found")

    def addLabels(self):
        self.score_label.setAlignment(QtCore.Qt.AlignRight)
        self.score_label.setStyleSheet(
            "font-size: 35px;" +
            "color: 'white';" +
            "padding: 20px 15px 20px 5px;" +
            "margin: 20px 200px;" +
            "background: '#64A314';" +
            "border: 1px solid '#64A314';" +
            "border-radius: 38px;"
        )
        self.score_label.setWordWrap(True)
        self.layout().addWidget(self.score_label, 0, 1)

        question = QLabel(parameters["question"][-1], self)
        question.setAlignment(QtCore.Qt.AlignCenter)
        question.setWordWrap(True)
        question.setStyleSheet(
            "font-family: Shanti;" +
            "font-size: 25px;" +
            "color: 'white';"+
            "padding: 75px;"
        )
        self.layout().addWidget(question, 1, 0, 1, 2)

    def addButton(self):
        button1 = self.create_button(parameters["answer1"][-1], 85, 5)
        button2 = self.create_button(parameters["answer2"][-1], 5, 85)
        button3 = self.create_button( parameters["answer3"][-1], 85, 5)
        button4 = self.create_button( parameters["answer4"][-1], 5, 85)
        self.layout().addWidget(button1, 2,0)
        self.layout().addWidget(button2, 2, 1)
        self.layout().addWidget(button3, 3, 0)
        self.layout().addWidget(button4, 3, 1)


    def create_button(self, answer, l_margin, r_margin):
        button = QPushButton(answer)
        button.setCursor(QtCore.Qt.PointingHandCursor)
        button.setFixedWidth(485)
        button.setStyleSheet(
            "*{border: 4px solid '#BC006C';" +
            "margin-left: " + str(l_margin) + "px;" +
            "margin-right: " + str(r_margin) + "px;" +
            "color: 'white';" +
            "font-family: 'Shanti';" +
            "font-size: 16px;" +
            "padding: 15px 0;" +
            "border-radius: 20px;"
            "margin-top: 20px;}" +
            "*:hover{ background: '#BC006C' }"
        )
        button.clicked.connect(lambda x: self.is_correct(answer))
        return button

    def is_correct(self, answer):
        if(answer == parameters["correct"][-1]):
            print("You Win!!")
            self.score += 10

            if(self.score >= 50):
                self.child_view = win_frame.EndGame(self.score)
                self.hide()
                self.child_view.show()
            else:
               self.reload_data()

        else:
            self.score -= 10
            if(self.score < 0):
                self.child_view = loose_frame.LooseWindow(self.score)
                self.hide()
                self.child_view.show()
            else:
                self.reload_data()

    def reload_data(self):
        self.score_label.setText(str(self.score))
        preload_data(random.randint(0, 49))
        self.addButton()
        self.addLabels()

