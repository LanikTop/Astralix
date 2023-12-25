import pygame
import os
import sys
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
        # Параметры корабля
        self.speed = 2
        self.shoot_speed = 1
        self.shoot_count = 1
        self.hp = 1
        # Создание корабля
        self.all_sprites = pygame.sprite.Group()
        self.ship = pygame.sprite.Sprite()
        self.ship.image = load_image('ship.png', -1)
        self.ship.image = pygame.transform.scale(self.ship.image, (150, 150))
        self.ship.rect = self.ship.image.get_rect()
        self.all_sprites.add(self.ship)
        self.ship.rect.x = size1 // 2 - 75
        self.ship.rect.y = int(size2 * 0.8)

    def get_damage(self, damage):
        self.hp -= damage

    def move_ship(self, move_x, move_y):
        self.ship.rect.x += move_x
        self.ship.rect.y += move_y


class Bullet:
    def __init__(self, size1, size2, sprite):
        self.all_sprites = sprite
        self.bullet = pygame.sprite.Sprite()
        self.bullet.image = load_image('bullet.png', -1)
        self.bullet.image = pygame.transform.scale(self.bullet.image, (150, 150))
        self.bullet.rect = self.bullet.image.get_rect()
        self.all_sprites.add(self.bullet)
        self.bullet.rect.x = size1
        self.bullet.rect.y = size2


class Meteor:
    def __init__(self, size1, sprite):
        self.size1 = size1
        self.meteor = pygame.sprite.Sprite()
        self.meteor.image = load_image('meteor_1.png', -1)
        self.meteor.image = pygame.transform.scale(self.meteor.image, (120, 120))
        self.meteor.rect = self.meteor.image.get_rect()
        sprite.add(self.meteor)
        self.meteor.rect.x = choice(range(size1))
        self.meteor.rect.y = -20


def start_game_buttle():
    # Создание окна
    pygame.init()
    screen = pygame.display.set_mode([1000, 700])
    width = screen.get_width()
    height = screen.get_height()
    backround = load_image('backround.png', -1)
    running = True
    ship = SpaceShip(width, height)
    mouse_down = False
    go_move = False
    bullets = pygame.sprite.Group()
    meteorits = pygame.sprite.Group()
    timer_shoots = 0
    timer_meteors = 0
    way_ship = ship.speed
    way_bullet = 0.7
    way_meteor = 0.51
    life = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_down = True
            if event.type == pygame.MOUSEMOTION and mouse_down:
                x, y = event.pos[0] - 75, event.pos[1] - 75
                if not go_move:
                    go_move = True
            if event.type == pygame.MOUSEBUTTONUP:
                mouse_down = False
        for elem in meteorits:
            if pygame.sprite.collide_mask(ship.ship, elem):
                life = False
        if life:
            if go_move and ship.ship.rect.x == x and ship.ship.rect.y == y:
                go_move = False
            if go_move:
                if ship.ship.rect.x < x:
                    ship.move_ship(way_ship, 0)
                    if ship.ship.rect.x > x:
                        ship.ship.rect.x = x
                if ship.ship.rect.x > x:
                    ship.move_ship(-way_ship, 0)
                    if ship.ship.rect.x < x:
                        ship.ship.rect.x = x
                if ship.ship.rect.y < y:
                    ship.move_ship(0, way_ship)
                    if ship.ship.rect.y > y:
                        ship.ship.rect.y = y
                if ship.ship.rect.y > y:
                    ship.move_ship(0, -way_ship)
                    if ship.ship.rect.y < y:
                        ship.ship.rect.y = y
            timer_shoots += 1
            if timer_shoots > 500:
                Bullet(ship.ship.rect.x + 6, ship.ship.rect.y, bullets)
                timer_shoots = 0
            timer_meteors += 1
            if timer_meteors > 2000:
                Meteor(width, meteorits)
                timer_meteors = 0
            screen.fill((0, 0, 0))
            screen.blit(backround, (0, 0))
            ship.all_sprites.draw(screen)
            for elem in bullets:
                elem.rect.y -= way_bullet
                if elem.rect.y < -100:
                    elem.kill()
                else:
                    for elem2 in meteorits:
                        if pygame.sprite.collide_mask(elem, elem2):
                            elem2.kill()
                            elem.kill()
            for elem in meteorits:
                elem.rect.y += way_meteor
                if elem.rect.y > height:
                    elem.kill()
            meteorits.draw(screen)
            bullets.draw(screen)
        else:
            screen.fill((0, 0, 0))
            gameover_image = load_image('gameover.png', -1)
            gameover_image = pygame.transform.scale(gameover_image, (1000, 700))
            screen.blit(gameover_image, (0, 0))
        pygame.display.flip()
    sys.exit()
