from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon


class Ui_Rules_Window(object):
    def rules_window_Ui(self, Rules_Window):
        Rules_Window.setObjectName("Rules_Window")
        Rules_Window.resize(969, 689)
        self.background = QtWidgets.QLabel(Rules_Window)
        self.background.setGeometry(QtCore.QRect(-30, -130, 1201, 951))
        self.background.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap("data/maxresdefault.jpg"))
        self.background.setObjectName("background")
        self.label = QtWidgets.QLabel(Rules_Window)
        self.label.setGeometry(QtCore.QRect(60, 210, 901, 671))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("data/text.png"))
        self.label.setObjectName("label")
        self.go_back_button = QtWidgets.QPushButton(Rules_Window)
        self.go_back_button.setGeometry(QtCore.QRect(10, 10, 75, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.go_back_button.setFont(font)
        self.go_back_button.setStyleSheet("border-radius : 50; \n"
                                          "color: rgb(255, 255, 255);\n"
                                          "border : 2px solid white\n"
                                          "")
        self.go_back_button.setObjectName("go_back_button")

        self.retranslateUi(Rules_Window)
        QtCore.QMetaObject.connectSlotsByName(Rules_Window)

    def retranslateUi(self, Rules_Window):
        _translate = QtCore.QCoreApplication.translate
        Rules_Window.setWindowTitle(_translate("Rules_Window", "Astralix"))
        Rules_Window.setWindowIcon(QIcon('data\pngwing.png'))
        self.go_back_button.setText(_translate("Rules_Window", "Back"))
