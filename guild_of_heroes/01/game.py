import sys
import pygame
from pygame import *
from screen_texts import win
from player import *
from blocks import *

WIN_WIDTH = 800
WIN_HEIGHT = 600
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)
BACKGROUND_IMAGE1 = pygame.image.load('forest_bg.png')
BACKGROUND_IMAGE1 = pygame.transform.scale(BACKGROUND_IMAGE1,
                                           (WIN_WIDTH, WIN_HEIGHT))
lvls = ["map_1.txt", "map_2.txt"]
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
    l = min(0, l)
    l = max(-(camera.width - WIN_WIDTH), l)
    t = max(-(camera.height - WIN_HEIGHT), t)
    t = min(0, t)
    return Rect(l, t, w, h)


def loadLevel(lvl):
    global playerX, playerY, level, platforms, entities  # объявляем глобальные переменные, это координаты героя

    levelFile = open(lvls[lvl])
    line = " "
    level, platforms = [], []
    entities = pygame.sprite.Group()
    commands = []
    while line[0] != "/":
        line = levelFile.readline()
        if line[0] == "[":
            while line[0] != "]":
                line = levelFile.readline()
                if line[0] != "]":
                    endLine = line.find("|")
                    level.append(line[0: endLine])
        if line[0] != "":
            commands = line.split()
            if len(commands) > 1:
                if commands[0] == "player":
                    playerX = int(commands[1])
                    playerY = int(commands[2])
    levelFile.close()


class Button:
    def __init__(self, text, x, y, width, height, color, hover_color):
        self.text = text
        self.rect = Rect(x, y, width, height)
        self.color = color
        self.hover_color = hover_color
        self.font = pygame.font.Font(None, 36)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        text_surface = self.font.render(self.text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)

    def is_hovered(self, pos):
        return self.rect.collidepoint(pos)


def main():
    global current_lvl
    loadLevel(current_lvl)

    # Инициализация Pygame и экран
    pygame.init()
    screen = pygame.display.set_mode(DISPLAY)
    pygame.display.set_caption("Guild of Heroes")

    # Инициализация глобальных переменных
    global entities, animatedEntities, monsters, platforms
    entities = pygame.sprite.Group()
    animatedEntities = pygame.sprite.Group()
    monsters = pygame.sprite.Group()
    platforms = []

    left = right = False
    up = False
    running = False
    hero = Player(playerX, playerY, WIN_HEIGHT, screen)  # создаем героя по (x,y) координатам
    entities.add(hero)
    timer = pygame.time.Clock()
    x = y = 0
    exit_button = Button("Выйти", 500, 540, 100, 50, (50, 128, 68), (0, 0, 0))

    for row in level:
        for col in row:
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
            x += PLATFORM_WIDTH
        y += PLATFORM_HEIGHT
        x = 0

    total_level_width = len(level[0]) * PLATFORM_WIDTH
    total_level_height = len(level) * PLATFORM_HEIGHT
    camera = Camera(camera_configure, total_level_width, total_level_height)
    start_time = pygame.time.get_ticks()

    while not hero.winner:
        timer.tick(60)
        for e in pygame.event.get():
            if e.type == QUIT:
                pygame.quit()
                sys.exit()
            if e.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if exit_button.is_hovered(mouse_pos):
                    from menu import MenuWindow
                    menu_window = MenuWindow()
                    menu_window.run()

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
        animatedEntities.update()
        camera.update(hero)
        hero.update(left, right, up, platforms)

        for e in entities:
            screen.blit(e.image, camera.apply(e))

        current_time = pygame.time.get_ticks()
        elapsed_time = current_time - start_time
        font = pygame.font.Font("DreiFraktur.ttf", 17)
        text = font.render(f"Время: {elapsed_time // 1000} сек", True,
                           (50, 128, 68))
        screen.blit(text, (623, 562))

        exit_button.draw(screen)

        pygame.display.update()

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
            pygame.display.update()


if __name__ == "__main__":
    main()
