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
        self.showMaximized()
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
        self.showMaximized()
        self.go_back_button.clicked.connect(self.go_back_start_window)

    def go_back_start_window(self):
        self.start_ex = Start_Window()
        self.start_ex.show()
        self.close()


PRICE_PLAYER_SPEED = 2
PRICE_SHOOT_RATE = 2
PRICE_SHOOT_SPEED = 2

COUNT_PS = 1
COUNT_SR = 1
COUNT_SS = 1


class Shop_Window(QDialog, Ui_Shop_Window):
    def __init__(self):
        super().__init__()
        self.shop_window_Ui(self)
        self.showMaximized()
        self.con = sqlite3.connect("player_data.db")
        self.cur = self.con.cursor()

        self.balance = self.cur.execute('''SELECT money FROM info_users WHERE id=1''').fetchone()[0]
        self.player_speed_value = self.cur.execute('''SELECT player_speed FROM info_users WHERE id=1''').fetchone()[0]
        self.shoot_rate_value = self.cur.execute('''SELECT shoot_rate FROM info_users WHERE id=1''').fetchone()[0]
        self.shoot_speed_value = self.cur.execute('''SELECT shoot_speed FROM info_users WHERE id=1''').fetchone()[0]

        self.level_1.setText(f'Уровень {self.player_speed_value}')
        self.level_2.setText(f'Уровень {self.shoot_rate_value}')
        self.level_3.setText(f"Уровень {self.shoot_speed_value}")

        self.player_speed_level_1.setText(f'{2 ** self.player_speed_value} pl')
        self.shoot_rate_level_1.setText(f'{2 ** self.shoot_rate_value} sr')
        self.shoot_speed_level_1.setText(f'{2 ** self.shoot_speed_value} ss')

        self.go_back_button.clicked.connect(self.go_back)

        self.player_speed_level_1.clicked.connect(self.buy_boost)
        self.player_speed_level_1.setIcon(QtGui.QIcon('data\money.png'))
        self.player_speed_level_1.setIconSize(QtCore.QSize(40, 40))

        self.shoot_rate_level_1.clicked.connect(self.buy_boost)
        self.shoot_rate_level_1.setIcon(QtGui.QIcon('data\money.png'))
        self.shoot_rate_level_1.setIconSize(QtCore.QSize(40, 40))

        self.shoot_speed_level_1.clicked.connect(self.buy_boost)
        self.shoot_speed_level_1.setIcon(QtGui.QIcon('data\money.png'))
        self.shoot_speed_level_1.setIconSize(QtCore.QSize(40, 40))

        self.check_balance.setText(str(self.balance))
        self.no_money_label.hide()

    def buy_boost(self):
        global PRICE_SHOOT_RATE
        global PRICE_SHOOT_SPEED
        global PRICE_PLAYER_SPEED

        global COUNT_PS
        global COUNT_SR
        global COUNT_SS

        button = QApplication.instance().sender()
        text = button.text().split()

        if self.balance >= int(text[0]):
            # player speed ↓ ↓ ↓ ↓
            if text[1] == 'pl':
                self.cur.execute('''UPDATE info_users SET player_speed=player_speed+1 WHERE id=1''')
                self.cur.execute('''UPDATE info_users SET money=money - ? WHERE id=1''', (PRICE_PLAYER_SPEED,))
                self.balance -= PRICE_PLAYER_SPEED
                self.check_balance.setText(str(self.balance))
                COUNT_PS += 1
                PRICE_PLAYER_SPEED = 2 ** COUNT_PS
                self.player_speed_level_1.setText(f'{PRICE_PLAYER_SPEED} pl')
                self.level_1.setText(f"Уровень {COUNT_PS}")
                self.con.commit()
            # shoot rate ↓ ↓ ↓ ↓
            elif text[1] == 'sr':
                self.cur.execute('''UPDATE info_users SET shoot_rate=shoot_rate+1 WHERE id=1''')
                self.cur.execute('''UPDATE info_users SET money=money - ? WHERE id=1''', (PRICE_SHOOT_RATE,))
                self.balance -= PRICE_SHOOT_RATE
                self.check_balance.setText(str(self.balance))
                COUNT_SR += 1
                PRICE_SHOOT_RATE = 2 ** COUNT_SR
                self.shoot_rate_level_1.setText(f'{PRICE_SHOOT_RATE} sr')
                self.level_2.setText(f"Уровень {COUNT_SR}")
                self.con.commit()
            # shoot_speed ↓ ↓ ↓ ↓
            elif text[1] == 'ss':
                self.cur.execute('''UPDATE info_users SET shoot_speed=shoot_speed+1 WHERE id=1''')
                self.cur.execute('''UPDATE info_users SET money=money - ? WHERE id=1''', (PRICE_SHOOT_SPEED,))
                self.balance -= PRICE_SHOOT_SPEED
                self.check_balance.setText(str(self.balance))
                COUNT_SS += 1
                PRICE_SHOOT_SPEED = 2 ** COUNT_SS
                self.shoot_speed_level_1.setText(f'{PRICE_SHOOT_SPEED} ss')
                self.level_3.setText(f"Уровень {COUNT_SS}")
                self.con.commit()
        else:
            self.print_no_money()

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
