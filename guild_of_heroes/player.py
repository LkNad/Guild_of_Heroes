import pygame.sprite
from pygame import *

import blocks
from loader import load_image

MOVE_SPEED = 7
WIDTH = 61
HEIGHT = 125
COLOR = "#888888"
JUMP_POWER = 10
GRAVITY = 0.35  # Сила, которая будет тянуть нас вниз


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.xvel = 0  # скорость перемещения. 0 - стоять на месте
        self.startX = x  # Начальная позиция Х, пригодится когда будем переигрывать уровень
        self.startY = y
        self.yvel = 0  # скорость вертикального перемещения
        self.onGround = False  # На земле ли я?
        self.right = False  # проверка какой стороной я стою
        self.image = Surface((WIDTH, HEIGHT))
        self.rect = Rect(x, y, WIDTH, HEIGHT)  # прямоугольный объект
        self.image.set_colorkey(Color(COLOR))  # делаем фон прозрачным
        # Загрузка картинок
        self.left_image = pygame.image.load("7_ch.png")
        self.right_step_image = pygame.image.load("7_ch_step.png")
        self.left_step_image = pygame.transform.flip(self.right_step_image, True, False)
        self.image = self.left_image  # по умолчанию
        self.winner = False

    def update(self, left, right, up, platforms):

        if up:
            if self.onGround:  # прыгаем, только когда можем оттолкнуться от земли
                self.yvel = -JUMP_POWER

        if left:
            self.xvel = -MOVE_SPEED  # Лево = x- n
            self.image = self.left_step_image

        if right:
            self.xvel = MOVE_SPEED  # Право = x + n
            self.image = self.right_step_image

        if not (left or right):  # стоим, когда нет указаний идти
            self.xvel = 0
            self.image = self.left_image

        if not self.onGround:
            self.yvel += GRAVITY

        self.onGround = False  # когда мы не на земле
        self.rect.y += self.yvel
        self.collide(0, self.yvel, platforms)

        self.rect.x += self.xvel  # переносим свои положение на xvel
        self.collide(self.xvel, 0, platforms)

    def collide(self, xvel, yvel, platforms):
        for p in platforms:
            if sprite.collide_rect(self, p):  # если есть пересечение платформы с игроком
                if isinstance(p, blocks.Next_level):  # если коснулись принцессы
                    self.winner = True  # победили!!!
                else:
                    if xvel > 0:  # если движется вправо
                        self.rect.right = p.rect.left  # то не движется вправо

                    if xvel < 0:  # если движется влево
                        self.rect.left = p.rect.right  # то не движется влево

                    if yvel > 0:  # если падает вниз
                        self.rect.bottom = p.rect.top  # то не падает вниз
                        self.onGround = True  # и становится на что-то твердое
                        self.yvel = 0  # и энергия падения пропадает

                    if yvel < 0:  # если движется вверх
                        self.rect.top = p.rect.bottom  # то не движется вверх
                        self.yvel = 0
