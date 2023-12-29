import sys
from start_window import Ui_Start_Window
from rules_window import Ui_Rules_Window
from shop_window import Ui_Shop_Window
from SpaceShip import *
import sqlite3

from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QWidget, QPushButton, QVBoxLayout, QLabel, QFileDialog, \
    QListWidgetItem

from PyQt5 import QtGui, QtCore


class Start_Window(QMainWindow, Ui_Start_Window):
    def __init__(self):
        super().__init__()
        self.start_window_Ui(self)

        self.rules_button.clicked.connect(self.open_rules_window)
        self.start_game_button.clicked.connect(self.start_game)
        self.shop_button.clicked.connect(self.open_shop_window)

    def open_shop_window(self):
        self.shop_ex = Shop_Window()
        self.shop_ex.show()
        self.close()

    def open_rules_window(self):
        self.rules_ex = Rules_Window()
        self.rules_ex.show()
        self.close()

    def start_game(self):
        self.hide()
        start_game_buttle()
        self.show()


class Rules_Window(QDialog, Ui_Rules_Window):
    def __init__(self):
        super().__init__()
        self.rules_window_Ui(self)

        self.go_back_button.clicked.connect(self.go_back_start_window)

    def go_back_start_window(self):
        self.start_ex = Start_Window()
        self.start_ex.show()
        self.close()

class Shop_Window(QDialog, Ui_Shop_Window):
    def __init__(self):
        super().__init__()
        self.shop_window_Ui(self)

        con = sqlite3.connect("player_data.db")
        cur = con.cursor()

        self.balance = cur.execute('''SELECT money FROM info_users WHERE id=1''').fetchone()[0]
        self.go_back_button.clicked.connect(self.go_back)
        self.pushButton_1.clicked.connect(self.print_no_money)
        self.pushButton_1.setIcon(QtGui.QIcon('data\money.png'))
        self.pushButton_1.setIconSize(QtCore.QSize(40, 40))

        self.pushButton_2.clicked.connect(self.print_no_money)
        self.pushButton_2.setIcon(QtGui.QIcon('data\money.png'))
        self.pushButton_2.setIconSize(QtCore.QSize(40, 40))

        self.pushButton_3.clicked.connect(self.print_no_money)
        self.pushButton_3.setIcon(QtGui.QIcon('data\money.png'))
        self.pushButton_3.setIconSize(QtCore.QSize(40, 40))

        self.pushButton_4.clicked.connect(self.print_no_money)
        self.pushButton_4.setIcon(QtGui.QIcon('data\money.png'))
        self.pushButton_4.setIconSize(QtCore.QSize(40, 40))

        self.pushButton_5.clicked.connect(self.print_no_money)
        self.pushButton_5.setIcon(QtGui.QIcon('data\money.png'))
        self.pushButton_5.setIconSize(QtCore.QSize(40, 40))

        self.pushButton_6.clicked.connect(self.print_no_money)
        self.pushButton_6.setIcon(QtGui.QIcon('data\money.png'))
        self.pushButton_6.setIconSize(QtCore.QSize(40, 40))

        self.check_balance.setText(str(self.balance))
        self.no_money_label.hide()

    def print_no_money(self):
        self.no_money_label.show()
    def go_back(self):
        self.start_ex = Start_Window()
        self.start_ex.show()
        self.close()





if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Start_Window()
    ex.show()
    sys.exit(app.exec())
