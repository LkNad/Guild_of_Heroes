import os
import sys

import pygame

pygame.init()
pygame.key.set_repeat(200, 70)
size = width, height = 500, 500
screen = pygame.display.set_mode(size)
FPS = 50
JUMP_POWER = 30 # сила с которой прыгает персонаж
GRAVITY = 0.1  # гравитация
clock = pygame.time.Clock()


def terminate():
    pygame.quit()
    sys.exit()


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
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


def start_screen():
    intro_text = ["ЗАСТАВКА", "",
                  "Правила игры",
                  "Если в правилах несколько строк,",
                  "приходится выводить их построчно"]

    fon = pygame.transform.scale(load_image('fon.jpg'), (width, height))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 70
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('red'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return  # начинаем игру
        pygame.display.flip()
        clock.tick(FPS)


def load_level(filename):
    filename = "data/" + filename
    # читаем уровень, убирая символы перевода строки
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]

    # и подсчитываем максимальную длину
    max_width = max(map(len, level_map))

    # дополняем каждую строку пустыми клетками ('.')
    return list(map(lambda x: x.ljust(max_width, '.'), level_map))


tile_images = {
    'wall': load_image('box.png'),
    'empty': load_image('ggrass0.png')
}
player_image = load_image('mag1.png')

tile_width = tile_height = 50

# основной персонаж
player = None

# группы спрайтов
all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
wall_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()


def generate_level(level):
    new_player, x, y = None, None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '.':
                Tile('empty', x, y)
            elif level[y][x] == '#':
                Tile('wall', x, y)
            elif level[y][x] == '@':
                Tile('empty', x, y)
                new_player = Player(x, y)
    # вернем игрока, а также размер поля в клетках
    return new_player, x, y


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        if tile_type == 'wall':
            super().__init__(tiles_group, all_sprites, wall_group)
        else:
            super().__init__(tiles_group, all_sprites)
        self.image = tile_images[tile_type]
        self.tile_type = tile_type
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(player_group, all_sprites)
        self.image = player_image
        self.tile_type = "player"
        self.rect = self.image.get_rect().move(
            tile_width * pos_x + 15, tile_height * pos_y + 7)
        self.velocity = 0
        self.gravity = GRAVITY

    # прыгать
    def jump(self):
        self.rect.y += JUMP_POWER
        if (pygame.sprite.groupcollide(player_group, wall_group, False,
                                       False) or not (
        pygame.sprite.groupcollide(tiles_group, player_group, False, False))):
            self.rect.y -= JUMP_POWER
        else:
            for i in range(10):
                self.rect.y -= JUMP_POWER * GRAVITY
                all_sprites.update()

                screen.fill(pygame.Color(71, 116, 12))
                camera.update(player)
                for sprite in all_sprites:
                    camera.apply(sprite)

                tiles_group.draw(screen)
                player_group.draw(screen)
                pygame.display.flip()

                clock.tick(FPS*1.2)
        clock.tick(FPS*5)


    def update_jump(self):
        # применяем гравитационный эффект:
        # движение с ускорением под действием гравитации

        if not (pygame.sprite.groupcollide(player_group, wall_group,
                                           False,
                                           False)):
            self.velocity += self.gravity
            self.rect.y += self.velocity
        elif pygame.sprite.groupcollide(tiles_group, player_group, False,
                                        False):
            self.velocity += self.gravity
            self.rect.y += self.velocity
        else:
            self.velocity -= self.gravity
            self.rect.y -= self.velocity


class Camera:
    # зададим начальный сдвиг камеры
    def __init__(self):
        self.dx = 0
        self.dy = 0

    # сдвинуть объект obj на смещение камеры
    def apply(self, obj):
        obj.rect.x += self.dx
        obj.rect.y += self.dy

    # позиционировать камеру на объекте target
    def update(self, target):
        self.dx = -(target.rect.x + target.rect.w // 2 - width // 2)
        self.dy = -(target.rect.y + target.rect.h // 2 - height // 2)


start_screen()
player, level_x, level_y = generate_level(load_level('road.txt'))
running = True
STEP = 10

player = Player(0, 1.5)  # Спавн игрока
camera = Camera()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if pygame.key.get_mods() == 4097:
                    player.rect.x -= STEP * 2
                    if pygame.sprite.groupcollide(player_group, wall_group,
                                                  False,
                                                  False):
                        player.rect.x += STEP * 2
                    elif not (
                            pygame.sprite.groupcollide(tiles_group,
                                                       player_group, False,
                                                       False)):
                        player.rect.x += STEP * 4
                else:
                    player.rect.x -= STEP
                    if pygame.sprite.groupcollide(player_group, wall_group,
                                                  False,
                                                  False):
                        player.rect.x += STEP
                    elif not (
                            pygame.sprite.groupcollide(tiles_group,
                                                       player_group, False,
                                                       False)):
                        player.rect.x += STEP * 2
            if event.key == pygame.K_RIGHT:
                if pygame.key.get_mods() == 4097:
                    player.rect.x += STEP * 2
                    if pygame.sprite.groupcollide(player_group, wall_group,
                                                  False,
                                                  False):
                        player.rect.x -= STEP * 2
                    elif not (
                            pygame.sprite.groupcollide(tiles_group,
                                                       player_group, False,
                                                       False)):
                        player.rect.x -= STEP * 4
                else:
                    player.rect.x += STEP
                    if pygame.sprite.groupcollide(player_group, wall_group,
                                                  False,
                                                  False):
                        player.rect.x -= STEP
                    elif not (
                            pygame.sprite.groupcollide(tiles_group,
                                                       player_group, False,
                                                       False)):
                        player.rect.x -= STEP * 2
            if event.key == pygame.K_UP or event.key == pygame.K_SPACE:
                if pygame.sprite.groupcollide(player_group, wall_group,
                                              False,
                                              False) or not (
                        pygame.sprite.groupcollide(tiles_group,
                                                   player_group, False,
                                                   False)):
                    player.jump()
                else:
                    JUMP_POWER = -JUMP_POWER
                    player.jump()
                    JUMP_POWER = -JUMP_POWER
                # функция прыганья
            all_sprites.update()

    screen.fill(pygame.Color(71, 116, 12))
    camera.update(player)
    for sprite in all_sprites:
        camera.apply(sprite)

    tiles_group.draw(screen)
    player_group.draw(screen)
    pygame.display.flip()

    clock.tick(FPS)
terminate()
