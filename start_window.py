from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon


class Ui_Start_Window(object):
    def start_window_Ui(self, Start_Window):
        Start_Window.setObjectName("Start_Window")
        Start_Window.resize(970, 690)
        self.background = QtWidgets.QLabel(Start_Window)
        self.background.setGeometry(QtCore.QRect(-170, -130, 1201, 951))
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap("data/maxresdefault.jpg"))
        self.background.setObjectName("background")
        self.name_of_the_game_lb = QtWidgets.QLabel(Start_Window)
        self.name_of_the_game_lb.setGeometry(QtCore.QRect(250, 180, 521, 131))
        font = QtGui.QFont()
        font.setFamily("Minecraft Seven Cyrillic (russi")
        font.setPointSize(80)
        self.name_of_the_game_lb.setFont(font)
        self.name_of_the_game_lb.setStyleSheet("color: rgb(255, 255, 255);\n"
"")
        self.name_of_the_game_lb.setObjectName("name_of_the_game_lb")
        self.start_game_button = QtWidgets.QPushButton(Start_Window)
        self.start_game_button.setGeometry(QtCore.QRect(370, 390, 231, 61))
        font = QtGui.QFont()
        font.setFamily("Minecraft Seven Cyrillic (russi")
        font.setPointSize(25)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.start_game_button.setFont(font)
        self.start_game_button.setStyleSheet("background-color: rgb(26, 66, 117);\n"
"color: rgb(114, 177, 255);")
        self.start_game_button.setObjectName("start_game_button")
        self.rules_button = QtWidgets.QPushButton(Start_Window)
        self.rules_button.setEnabled(True)
        self.rules_button.setGeometry(QtCore.QRect(370, 470, 231, 61))
        font = QtGui.QFont()
        font.setFamily("Minecraft Seven Cyrillic (russi")
        font.setPointSize(25)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.rules_button.setFont(font)
        self.rules_button.setStyleSheet("background-color: rgb(26, 66, 117);\n"
"color: rgb(114, 177, 255);")
        self.rules_button.setObjectName("rules_button")
        self.created_by_lb = QtWidgets.QLabel(Start_Window)
        self.created_by_lb.setGeometry(QtCore.QRect(10, 660, 201, 16))
        font = QtGui.QFont()
        font.setFamily("Minecraft Seven Cyrillic (russi")
        self.created_by_lb.setFont(font)
        self.created_by_lb.setStyleSheet("color: rgb(255, 255, 255);")
        self.created_by_lb.setObjectName("created_by_lb")

        self.retranslateUi(Start_Window)
        QtCore.QMetaObject.connectSlotsByName(Start_Window)

    def retranslateUi(self, Start_Window):
        _translate = QtCore.QCoreApplication.translate
        Start_Window.setWindowTitle(_translate("Start_Window", "Astralix"))
        Start_Window.setWindowIcon(QIcon('data\pngwing.png'))
        self.name_of_the_game_lb.setText(_translate("Start_Window", "Astralix"))
        self.start_game_button.setText(_translate("Start_Window", "Начать"))
        self.rules_button.setText(_translate("Start_Window", "Правила"))
        self.created_by_lb.setText(_translate("Start_Window", "created by Radmir and Ruslan"))
