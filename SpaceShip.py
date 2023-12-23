import pygame
import os
import sys

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


class SpaceShip():
    def __init__(self):
        # Параметры корабля
        self.speed = 1000
        self.shoot_speed = 1
        self.shoot_count = 1
        # Создание корабля
        self.all_sprites = pygame.sprite.Group()
        self.ship = pygame.sprite.Sprite()
        self.ship.image = load_image('ship.png', -1)
        self.ship.image = pygame.transform.scale(self.ship.image, (150, 150))
        self.ship.rect = self.ship.image.get_rect()
        self.all_sprites.add(self.ship)
        self.ship.rect.x = 400
        self.ship.rect.y = 700

    def get_damage(self, damage):
        self.hp -= damage

    def move_ship(self, move_x, move_y):
        way = self.speed * CLOCK.tick() / 1000
        self.ship.rect.x += move_x
        self.ship.rect.y += move_y

    def check_move(self, x, y):
        go_x = False
        go_y = False
        if self.ship.rect.x < x:
            self.move_ship(way, 0)
            if self.ship.rect.x > x:
                self.ship.rect.x = x
        if self.ship.rect.x > x:
            self.move_ship(-way, 0)
            if self.ship.rect.x < x:
                self.ship.rect.x = x
        if self.ship.rect.y < y:
            self.move_ship(0, way)
            if self.ship.rect.y > y:
                self.ship.rect.y = y
        if self.ship.rect.y > y:
            self.move_ship(0, -way)
            if self.ship.rect.y < y:
                self.ship.rect.y = y
        return go_x, go_y


def start_game_buttle():
    # Создание окна
    pygame.init()
    size = width, height = 1000, 700
    screen = pygame.display.set_mode(size)
    running = True
    ship = SpaceShip()
    mouse_down = False
    go_move = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_down = True
            if event.type == pygame.MOUSEMOTION and mouse_down:
                x, y = event.pos[0] - 75, event.pos[1] - 75
                if not go_move:
                    way = ship.speed * CLOCK.tick() / 1000
                    go_move = True
            if event.type == pygame.MOUSEBUTTONUP:
                mouse_down = False
        if go_move and ship.ship.rect.x == x and ship.ship.rect.y == y:
            go_move = False
        if go_move:
            if ship.ship.rect.x < x:
                ship.move_ship(way, 0)
                if ship.ship.rect.x > x:
                    ship.ship.rect.x = x
            if ship.ship.rect.x > x:
                ship.move_ship(-way, 0)
                if ship.ship.rect.x < x:
                    ship.ship.rect.x = x
            if ship.ship.rect.y < y:
                ship.move_ship(0, way)
                if ship.ship.rect.y > y:
                    ship.ship.rect.y = y
            if ship.ship.rect.y > y:
                ship.move_ship(0, -way)
                if ship.ship.rect.y < y:
                    ship.ship.rect.y = y
        screen.fill((0, 0, 0))
        ship.all_sprites.draw(screen)
        pygame.display.flip()

    sys.exit()


