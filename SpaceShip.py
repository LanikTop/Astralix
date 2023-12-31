import pygame
import os
import sys
import sqlite3
from random import choice

CLOCK = pygame.time.Clock()


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


class SpaceShip:
    def __init__(self, size1, size2):
        self.all_sprites = pygame.sprite.Group()
        self.ship = pygame.sprite.Sprite()
        self.ship.image = load_image('ship.png', -1)
        self.ship.image_top = pygame.transform.scale(self.ship.image, (150, 150))
        self.ship.image = pygame.transform.scale(self.ship.image, (150, 150))
        self.ship.image_left = pygame.transform.rotate(self.ship.image, -45)
        self.ship.image_right = pygame.transform.rotate(self.ship.image, 45)
        self.ship.rect = self.ship.image.get_rect()
        self.all_sprites.add(self.ship)
        self.ship.rect.x = size1 // 2 - 75
        self.ship.rect.y = int(size2 * 0.8)

    def move_ship(self, move_x, move_y):
        self.ship.rect.x += move_x
        self.ship.rect.y += move_y


class Bullet:
    def __init__(self, size1, size2, sprite):
        self.bullet = pygame.sprite.Sprite()
        self.bullet.image = load_image('bullet.png', -1)
        self.bullet.image = pygame.transform.scale(self.bullet.image, (150, 150))
        self.bullet.rect = self.bullet.image.get_rect()
        sprite.add(self.bullet)
        self.bullet.rect.x = size1
        self.bullet.rect.y = size2


class Meteor:
    def __init__(self, size1, sprite):
        self.meteor = pygame.sprite.Sprite()
        self.meteor.image = load_image('meteor_1.png', -1)
        self.meteor.image = pygame.transform.scale(self.meteor.image, (120, 120))
        self.meteor.rect = self.meteor.image.get_rect()
        sprite.add(self.meteor)
        self.meteor.rect.x = choice(range(size1 - 120))
        self.meteor.rect.y = -20


class Coin:
    def __init__(self, size1, sprite):
        self.coin = pygame.sprite.Sprite()
        self.coin.image = load_image('money.png', -1)
        self.coin.image = pygame.transform.scale(self.coin.image, (50, 50))
        self.coin.rect = self.coin.image.get_rect()
        sprite.add(self.coin)
        self.coin.rect.x = choice(range(size1 - 120))
        self.coin.rect.y = -20


def start_game_buttle(player=1):
    # Параметры игры
    con = sqlite3.connect("player_data.db")
    cur = con.cursor()
    result = cur.execute(f"""SELECT * FROM info_users WHERE id = {player}""").fetchone()
    money = result[1]
    player_speed = 10 + 10 * result[2]
    bullet_rate = 225 - 50 * result[3]
    bullet_speed = 6 + 3 * result[4]
    highscore = result[5]
    meteor_speed = 1
    # Создание окна
    pygame.init()
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    # Загрузка музыки
    pygame.mixer.music.load('sounds/space_sound.mp3')
    game_over_sound = pygame.mixer.Sound('sounds/game_over.ogg')
    # pygame.mixer.music.load('sounds/game_over.mp3')
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(-1)
    # Задний фон
    backround = load_image('backround.png', -1)
    backround = pygame.transform.scale(backround, screen.get_size())
    # Пауза
    pause = load_image('pause.png', -1)
    pause = pygame.transform.scale(pause, (150, 150))
    continuue = load_image('continue.png', -1)
    continuue = pygame.transform.scale(continuue, (screen.get_width() // 3, 150))
    quit = load_image('quit.png', -1)
    quit = pygame.transform.scale(quit, (screen.get_width() // 3, 150))
    # Корабль
    ship = SpaceShip(*screen.get_size())
    # Флаги переменные и группы перед началом
    mouse_down = False
    go_move = False
    bullets = pygame.sprite.Group()
    meteorits = pygame.sprite.Group()
    coins = pygame.sprite.Group()
    timer_shoots = 0
    timer_meteors = 0
    timer_coins = 0
    meteor_death_count = 0
    font_50 = pygame.font.Font(None, 40)
    score_text = font_50.render('SCORE', True, (255, 255, 255))
    font_10 = pygame.font.Font(None, 25)
    high_score_text = font_10.render('HIGH', True, (255, 255, 255))
    high_score = font_10.render(str(highscore), True, (255, 255, 255))
    life = True
    running = True
    flPause = False
    # Начало игры
    while running:
        pygame.time.delay(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_down = True
            if event.type == pygame.MOUSEBUTTONUP:
                if life is True and event.pos[0] >= (screen.get_width() - 150) and event.pos[1] <= 150:
                    life = 'pause'
                if life == 'pause' and screen.get_width() // 3 < event.pos[0] < (screen.get_width() * 2 // 3) and int(
                        screen.get_height() // 3.5) < event.pos[1] < int(screen.get_height() // 3.5) + 150:
                    life = True
                if life == 'pause' and screen.get_width() // 3 < event.pos[0] < (
                        screen.get_width() * 2 // 3) and screen.get_height() // 2 < event.pos[1] < (
                        screen.get_height() // 2 + 150):
                    life = 'exit'
                if not life and screen.get_width() // 2 < event.pos[0] < (screen.get_width() * 5 // 6) \
                        and int(screen.get_height() * 0.8) < event.pos[1] < int(screen.get_height() * 0.8) + 150:
                    life = 'exit'
                if not life and screen.get_width() // 10 < event.pos[0] < (screen.get_width() * 13 // 30) \
                        and int(screen.get_height() * 0.8) < event.pos[1] < int(screen.get_height() * 0.8) + 150:
                    life = 'restart'
            if event.type == pygame.MOUSEMOTION and mouse_down:
                x, y = event.pos[0] - 75, event.pos[1] - 75
                if not go_move:
                    go_move = True
            if event.type == pygame.MOUSEBUTTONUP:
                mouse_down = False
        # Проверка смерти
        for elem in meteorits:
            if pygame.sprite.collide_mask(ship.ship, elem) and life is True:
                life = False
        # Режим паузы
        if life == 'pause':
            pygame.mixer.music.pause()  # -> Поставить на паузу
            pygame.draw.rect(screen, pygame.Color((128, 128, 128)), (
                screen.get_width() // 4, screen.get_height() // 4, screen.get_width() // 2, screen.get_height() // 2))
            screen.blit(continuue, (screen.get_width() // 3, int(screen.get_height() // 3.5)))
            screen.blit(quit, (screen.get_width() // 3, screen.get_height() // 2))
        # Выход из игры
        elif life == 'exit':
            running = False
            cur.execute(f"""UPDATE info_users SET money = '{money}' WHERE id = '{player}'""")
        elif life == 'restart':
            running = False
            start_game_buttle()
        # Режим игры
        elif life:
            pygame.mixer.music.unpause()  # -> Снять паузу
            if go_move and ship.ship.rect.x == x and ship.ship.rect.y == y:
                go_move = False
            # Движение корабля
            if go_move:
                if ship.ship.rect.x < x:
                    ship.ship.image = ship.ship.image_left
                    ship.move_ship(player_speed, 0)
                    if ship.ship.rect.x > x:
                        ship.ship.image = ship.ship.image_top
                        ship.ship.rect.x = x
                if ship.ship.rect.x > x:
                    ship.ship.image = ship.ship.image_right
                    ship.move_ship(-player_speed, 0)
                    if ship.ship.rect.x < x:
                        ship.ship.image = ship.ship.image_top
                        ship.ship.rect.x = x
                if ship.ship.rect.y < y:
                    ship.move_ship(0, player_speed)
                    if ship.ship.rect.y > y:
                        ship.ship.rect.y = y
                if ship.ship.rect.y > y:
                    ship.move_ship(0, -player_speed)
                    if ship.ship.rect.y < y:
                        ship.ship.rect.y = y
            # Создание пули
            timer_shoots += 1
            if timer_shoots > bullet_rate:
                Bullet(ship.ship.rect.x + 6, ship.ship.rect.y, bullets)
                timer_shoots = 0
            # Создание метеорита
            timer_meteors += 1
            if timer_meteors > 500 - 20 * (meteor_death_count // 5):
                Meteor(screen.get_width(), meteorits)
                timer_meteors = 0
            # Создание монеты
            timer_coins += 1
            if timer_coins > 600:
                Coin(screen.get_width(), coins)
                timer_coins = 0
            # Движение пули
            for elem in bullets:
                elem.rect.y -= bullet_speed
                if elem.rect.y < -100:
                    elem.kill()
                else:
                    for elem2 in meteorits:
                        if pygame.sprite.collide_mask(elem, elem2):
                            elem2.kill()
                            elem.kill()
                            meteor_death_count += 1
            # Движение метеоритов
            for elem in meteorits:
                elem.rect.y += meteor_speed
                if elem.rect.y > screen.get_height():
                    elem.kill()
            # Движение монет
            for elem in coins:
                elem.rect.y += meteor_speed
                if elem.rect.y > screen.get_height():
                    elem.kill()
                if pygame.sprite.collide_mask(ship.ship, elem):
                    elem.kill()
                    money += 1
            # Новая отрисовка
            screen.fill((0, 0, 0))
            screen.blit(backround, (0, 0))
            ship.all_sprites.draw(screen)
            meteorits.draw(screen)
            coins.draw(screen)
            bullets.draw(screen)
            screen.blit(pause, (screen.get_width() - 160, 10))
            screen.blit(score_text, (0, 0))
            screen.blit(font_50.render(str(meteor_death_count), True, (255, 255, 255)), (40, 30))
            screen.blit(high_score_text, (12, 60))
            screen.blit(high_score, (70, 60))
            # Кнопка меню

        else:
            # Обновление бд
            cur.execute(f"""UPDATE info_users SET money = '{money}' WHERE id = '{player}'""")
            if highscore < meteor_death_count:
                cur.execute(f"""UPDATE info_users SET record = '{meteor_death_count}' WHERE id = '{player}'""")
            # gameover
            pygame.mixer.music.stop()
            game_over_sound.set_volume(0.1)
            game_over_sound.play(1)  # -> Звук game over

            screen.fill((0, 0, 0))
            gameover_image = load_image('gameover.png', -1)
            gameover_image = pygame.transform.scale(gameover_image, (screen.get_width(), screen.get_height() - 100))
            screen.blit(gameover_image, (0, 0))
            restart_image = load_image('restart.png', -1)
            restart_image = pygame.transform.scale(restart_image, (screen.get_width() // 3, 150))
            screen.blit(restart_image, (screen.get_width() // 10, int(screen.get_height() * 0.8)))
            screen.blit(quit, (screen.get_width() // 2, int(screen.get_height() * 0.8)))
        pygame.display.flip()
    game_over_sound.stop()
    con.commit()
    pygame.quit()
