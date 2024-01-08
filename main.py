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

        # player speed
        if self.player_speed_value == 2:
            self.player_speed_level_1.setEnabled(False)
        if 3 <= self.player_speed_value >= 2:
            self.player_speed_level_1.setEnabled(False)
            self.player_speed_level_2.setEnabled(False)
        if 4 <= self.player_speed_value >= 2:
            self.player_speed_level_1.setEnabled(False)
            self.player_speed_level_2.setEnabled(False)
            self.player_speed_level_3.setEnabled(False)
        # shoot rate
        if self.shoot_rate_value == 2:
            self.shoot_rate_level_1.setEnabled(False)
        if 3 <= self.shoot_rate_value >= 2:
            self.shoot_rate_level_1.setEnabled(False)
            self.shoot_rate_level_2.setEnabled(False)
        if 4 <= self.shoot_rate_value >= 2:
            self.shoot_rate_level_1.setEnabled(False)
            self.shoot_rate_level_2.setEnabled(False)
            self.shoot_rate_level_3.setEnabled(False)
        # shoot speed
        if self.shoot_speed_value == 2:
            self.shoot_speed_level_1.setEnabled(False)
        if 3 <= self.shoot_speed_value >= 2:
            self.shoot_speed_level_1.setEnabled(False)
            self.shoot_speed_level_2.setEnabled(False)
        if 4 <= self.shoot_speed_value >= 2:
            self.shoot_speed_level_1.setEnabled(False)
            self.shoot_speed_level_2.setEnabled(False)
            self.shoot_speed_level_3.setEnabled(False)


        self.go_back_button.clicked.connect(self.go_back)
        self.player_speed_level_1.clicked.connect(self.buy_boost)
        self.player_speed_level_1.setIcon(QtGui.QIcon('data\money.png'))
        self.player_speed_level_1.setIconSize(QtCore.QSize(40, 40))

        self.player_speed_level_2.clicked.connect(self.buy_boost)
        self.player_speed_level_2.setIcon(QtGui.QIcon('data\money.png'))
        self.player_speed_level_2.setIconSize(QtCore.QSize(40, 40))

        self.player_speed_level_3.clicked.connect(self.buy_boost)
        self.player_speed_level_3.setIcon(QtGui.QIcon('data\money.png'))
        self.player_speed_level_3.setIconSize(QtCore.QSize(40, 40))

        self.shoot_rate_level_1.clicked.connect(self.buy_boost)
        self.shoot_rate_level_1.setIcon(QtGui.QIcon('data\money.png'))
        self.shoot_rate_level_1.setIconSize(QtCore.QSize(40, 40))

        self.shoot_rate_level_2.clicked.connect(self.buy_boost)
        self.shoot_rate_level_2.setIcon(QtGui.QIcon('data\money.png'))
        self.shoot_rate_level_2.setIconSize(QtCore.QSize(40, 40))

        self.shoot_rate_level_3.clicked.connect(self.buy_boost)
        self.shoot_rate_level_3.setIcon(QtGui.QIcon('data\money.png'))
        self.shoot_rate_level_3.setIconSize(QtCore.QSize(40, 40))

        self.shoot_speed_level_1.clicked.connect(self.buy_boost)
        self.shoot_speed_level_1.setIcon(QtGui.QIcon('data\money.png'))
        self.shoot_speed_level_1.setIconSize(QtCore.QSize(40, 40))

        self.shoot_speed_level_2.clicked.connect(self.buy_boost)
        self.shoot_speed_level_2.setIcon(QtGui.QIcon('data\money.png'))
        self.shoot_speed_level_2.setIconSize(QtCore.QSize(40, 40))

        self.shoot_speed_level_3.clicked.connect(self.buy_boost)
        self.shoot_speed_level_3.setIcon(QtGui.QIcon('data\money.png'))
        self.shoot_speed_level_3.setIconSize(QtCore.QSize(40, 40))

        self.check_balance.setText(str(self.balance))
        self.no_money_label.hide()

    def buy_boost(self):
        button = QApplication.instance().sender()
        text = button.text().split()
        if self.balance >= int(text[0]):
            #player speed ↓ ↓ ↓ ↓
            if text[0] == '5' and text[1] == 'pl':
                self.cur.execute('''UPDATE info_users SET player_speed=2 WHERE id=1''')
                self.cur.execute('''UPDATE info_users SET money=money - ? WHERE id=1''', (int(text[0]),))
                self.balance -= 5
                self.check_balance.setText(str(self.balance))
                self.player_speed_level_1.setEnabled(False)
                self.con.commit()
            elif text[0] == '15' and text[1] == 'pl':
                self.cur.execute('''UPDATE info_users SET player_speed=3 WHERE id=1''')
                self.cur.execute('''UPDATE info_users SET money=money - ? WHERE id=1''', (int(text[0]),))
                self.balance -= 15
                self.check_balance.setText(str(self.balance))
                self.player_speed_level_2.setEnabled(False)
                self.con.commit()
            elif text[0] == '30' and text[1] == 'pl':
                self.cur.execute('''UPDATE info_users SET player_speed=4 WHERE id=1''')
                self.cur.execute('''UPDATE info_users SET money=money - ? WHERE id=1''', (int(text[0]),))
                self.balance -= 30
                self.check_balance.setText(str(self.balance))
                self.player_speed_level_3.setEnabled(False)
                self.con.commit()
            # shoot rate ↓ ↓ ↓ ↓
            elif text[0] == '5' and text[1] == 'sr':
                self.cur.execute('''UPDATE info_users SET shoot_rate=2 WHERE id=1''')
                self.cur.execute('''UPDATE info_users SET money=money - ? WHERE id=1''', (int(text[0]),))
                self.balance -= 5
                self.check_balance.setText(str(self.balance))
                self.shoot_rate_level_1.setEnabled(False)
                self.con.commit()
            elif text[0] == '15' and text[1] == 'sr':
                self.cur.execute('''UPDATE info_users SET shoot_rate=3 WHERE id=1''')
                self.cur.execute('''UPDATE info_users SET money=money - ? WHERE id=1''', (int(text[0]),))
                self.balance -= 15
                self.check_balance.setText(str(self.balance))
                self.shoot_rate_level_2.setEnabled(False)
                self.con.commit()
            elif text[0] == '30' and text[1] == 'sr':
                self.cur.execute('''UPDATE info_users SET shoot_rate=4 WHERE id=1''')
                self.cur.execute('''UPDATE info_users SET money=money - ? WHERE id=1''', (int(text[0]),))
                self.balance -= 30
                self.check_balance.setText(str(self.balance))
                self.shoot_rate_level_3.setEnabled(False)
                self.con.commit()
            # shoot_speed ↓ ↓ ↓ ↓
            elif text[0] == '5' and text[1] == 'ss':
                self.cur.execute('''UPDATE info_users SET shoot_speed=2 WHERE id=1''')
                self.cur.execute('''UPDATE info_users SET money=money - ? WHERE id=1''', (int(text[0]),))
                self.balance -= 5
                self.check_balance.setText(str(self.balance))
                self.shoot_speed_level_1.setEnabled(False)
                self.con.commit()
            elif text[0] == '15' and text[1] == 'ss':
                self.cur.execute('''UPDATE info_users SET shoot_speed=3 WHERE id=1''')
                self.cur.execute('''UPDATE info_users SET money=money - ? WHERE id=1''', (int(text[0]),))
                self.balance -= 15
                self.check_balance.setText(str(self.balance))
                self.shoot_speed_level_2.setEnabled(False)
                self.con.commit()
            elif text[0] == '30' and text[1] == 'ss':
                self.cur.execute('''UPDATE info_users SET shoot_speed=4 WHERE id=1''')
                self.cur.execute('''UPDATE info_users SET money=money - ? WHERE id=1''', (int(text[0]),))
                self.balance -= 30
                self.check_balance.setText(str(self.balance))
                self.shoot_speed_level_3.setEnabled(False)
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
