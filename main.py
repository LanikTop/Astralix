import sys
from start_window import Ui_Start_Window
from rules_window import Ui_Rules_Window
from SpaceShip import *

from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QWidget, QPushButton, QVBoxLayout, QLabel, QFileDialog, \
    QListWidgetItem


class Start_Window(QMainWindow, Ui_Start_Window):
    def __init__(self):
        super().__init__()
        self.start_window_Ui(self)

        self.rules_button.clicked.connect(self.open_rules_window)
        self.start_game_button.clicked.connect(self.start_game)

    def open_rules_window(self):
        self.rules_ex = Rules_Window()
        self.rules_ex.show()
        self.close()

    def start_game(self):
        self.hide()
        start_game_buttle()


class Rules_Window(QDialog, Ui_Rules_Window):
    def __init__(self):
        super().__init__()
        self.rules_window_Ui(self)

        self.go_back_button.clicked.connect(self.go_back_start_window)

    def go_back_start_window(self):
        self.start_ex = Start_Window()
        self.start_ex.show()
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Start_Window()
    ex.show()
    sys.exit(app.exec())
