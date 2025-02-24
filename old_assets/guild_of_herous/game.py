# Импортируем библиотеку pygame
import sys

import pygame
from pygame import *

from screen_texts import win
from player import *
from blocks import *
from monsters import *


# Объявляем переменные
WIN_WIDTH = 800  # Ширина создаваемого окна
WIN_HEIGHT = 600  # Высота
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)  # Группируем ширину и высоту в одну переменную
BACKGROUND_IMAGE1 = pygame.image.load('forest_bg.png')
BACKGROUND_IMAGE1 = pygame.transform.scale(BACKGROUND_IMAGE1, (WIN_WIDTH, WIN_HEIGHT))
lvls = ["map_1.txt", "map_2.txt", "map_3.txt"]
pygame.mixer.init()  # Инициализация микшера

pygame.mixer.music.load("Ready_for_Action.mp3")
pygame.mixer.music.play(-1)  # -1 означает бесконечное воспроизведение

current_lvl = 0


class Camera(object):
    def __init__(self, camera_func, width, height):
        self.camera_func = camera_func
        self.state = Rect(0, 0, width, height)

    def apply(self, target):
        return target.rect.move(self.state.topleft)

    def update(self, target):
        self.state = self.camera_func(self.state, target.rect)


def camera_configure(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    l, t = -l + WIN_WIDTH / 2, -t + WIN_HEIGHT / 2

    l = min(0, l)  # Не движемся дальше левой границы
    l = max(-(camera.width - WIN_WIDTH), l)  # Не движемся дальше правой границы
    t = max(-(camera.height - WIN_HEIGHT), t)  # Не движемся дальше нижней границы
    t = min(0, t)  # Не движемся дальше верхней границы

    return Rect(l, t, w, h)


def loadLevel(lvl):
    global playerX, playerY, level, platforms, entities  # объявляем глобальные переменные, это координаты героя

    levelFile = open(lvls[lvl])
    line = " "
    level, platforms = [], []
    entities = pygame.sprite.Group()
    commands = []
    while line[0] != "/":  # пока не нашли символ завершения файла
        line = levelFile.readline()  # считываем построчно
        if line[0] == "[":  # если нашли символ начала уровня
            while line[0] != "]":  # то, пока не нашли символ конца уровня
                line = levelFile.readline()  # считываем построчно уровень
                if line[0] != "]":  # и если нет символа конца уровня
                    endLine = line.find("|")  # то ищем символ конца строки
                    level.append(line[0: endLine])  # и добавляем в уровень строку от начала до символа "|"

        if line[0] != "":  # если строка не пустая
            commands = line.split()  # разбиваем ее на отдельные команды
            if len(commands) > 1:  # если количество команд > 1, то ищем эти команды
                if commands[0] == "player":  # если первая команда - player
                    playerX = int(commands[1])  # то записываем координаты героя
                    playerY = int(commands[2])
                if commands[0] == "monster":  # если первая команда monster, то создаем монстра
                    mn = Monster(int(commands[1]), int(commands[2]), int(commands[3]), int(commands[4]))
                    entities.add(mn)
                    platforms.append(mn)
                    monsters.add(mn)


def main():
    global current_lvl
    loadLevel(current_lvl)
    pygame.init()  # Инициация PyGame, обязательная строчка
    screen = pygame.display.set_mode(DISPLAY)  # Создаем окошко
    pygame.display.set_caption("Guild of Heroes")  # Пишем в шапку

    left = right = False  # по умолчанию - стоим
    up = False
    running = False

    hero = Player(playerX, playerY, WIN_HEIGHT, screen)  # создаем героя по (x,y) координатам
    entities.add(hero)

    timer = pygame.time.Clock()
    x = y = 0  # координаты

    for row in level:  # вся строка
        for col in row:  # каждый символ
            if col == "(":
                pf = Platform_1(x, y)
                entities.add(pf)
                platforms.append(pf)
            if col == "=":
                pf = Platform_2(x, y)
                entities.add(pf)
                platforms.append(pf)
            if col == "-":
                pf = Platform_4(x, y)
                entities.add(pf)
                platforms.append(pf)
            if col == ")":
                pf = Platform_3(x, y)
                entities.add(pf)
                platforms.append(pf)
            if col == "P":
                pr = Next_level(x, y)
                entities.add(pr)
                platforms.append(pr)

            x += PLATFORM_WIDTH  # блоки платформы ставятся на ширине блоков
        y += PLATFORM_HEIGHT  # то же самое и с высотой
        x = 0  # на каждой новой строчке начинаем с нуля

    total_level_width = len(level[0]) * PLATFORM_WIDTH  # Высчитываем фактическую ширину уровня
    total_level_height = len(level) * PLATFORM_HEIGHT  # высоту

    camera = Camera(camera_configure, total_level_width, total_level_height)
    start_time = pygame.time.get_ticks()  # Запоминаем начальное время
    while not hero.winner:  # Основной цикл программы
        timer.tick(60)
        for e in pygame.event.get():  # Обрабатываем события
            if e.type == QUIT:
                raise SystemExit
            if e.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                print(mouse_pos)
            if e.type == KEYDOWN and e.key == K_UP:
                up = True
            if e.type == KEYDOWN and e.key == K_SPACE:
                up = True
            if e.type == KEYDOWN and e.key == K_LEFT:
                left = True
            if e.type == KEYDOWN and e.key == K_RIGHT:
                right = True
            if e.type == KEYUP and e.key == K_UP:
                up = False
            if e.type == KEYUP and e.key == K_SPACE:
                up = False
            if e.type == KEYUP and e.key == K_RIGHT:
                right = False
            if e.type == KEYUP and e.key == K_LEFT:
                left = False

            if e.type == KEYDOWN and e.key == K_w:
                hero.winner = True
            if e.type == KEYDOWN and e.key == K_d:
                hero.rect.x = hero.startX
                hero.rect.y = hero.startY
                hurt(screen)

        screen.blit(BACKGROUND_IMAGE1, (0, 0))

        monsters.update(platforms)  # передвигаем всех монстров
        camera.update(hero)  # центризируем камеру относительно персонажа
        hero.update(left, right, up, platforms)  # передвижение
        for e in entities:
            screen.blit(e.image, camera.apply(e))
            # Получаем текущее время
        current_time = pygame.time.get_ticks()
        # Вычисляем прошедшее время
        elapsed_time = current_time - start_time
        font = pygame.font.Font("DreiFraktur.ttf", 17)
        text = font.render(f"Время: {elapsed_time // 1000} сек", True, (50, 128, 68))
        screen.blit(text, (623, 562))
        pygame.display.update()  # обновление и вывод всех изменений на экран

        if hero.winner:
            total_time = (pygame.time.get_ticks() - start_time) // 1000
            win(screen, total_time)
            if current_lvl >= len(lvls) - 1:
                pass
            else:
                hero.winner = False
                current_lvl += 1
                hero.kill()
                screen.fill((0, 0, 0))
                main()
                if current_lvl >= len(lvls) - 1:
                    return
            pygame.display.update()  # обновление и вывод всех изменений на экран


level = []
entities = pygame.sprite.Group()  # Все объекты
monsters = pygame.sprite.Group()  # Все передвигающиеся объекты
platforms = []  # то, во что мы будем врезаться или опираться
if __name__ == "__main__":
    main()
