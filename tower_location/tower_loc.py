import pygame
import sys
import pytmx

# Инициализация Pygame
pygame.init()
pygame.mixer.init()  # Инициализация микшера
width, height = 1920, 1020
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Тайловая карта с pytmx")
screen.fill((0,0,0))

# Загрузка тайловой карты
tmx_data = pytmx.load_pygame('tower_loc.tmx')
offset_x = 0
scroll_speed = 1
map_width = tmx_data.width * tmx_data.tilewidth
max_offset_x = map_width - width

pygame.mixer.music.load("data/music.mp3")
pygame.mixer.music.play(-1)  # -1 означает бесконечное воспроизведение

# Основной цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        offset_x += scroll_speed
        if offset_x > max_offset_x:  # Проверка на границы карты
            offset_x = max_offset_x

    if keys[pygame.K_LEFT]:
        offset_x -= scroll_speed
        if offset_x < 0:  # Проверка на границы карты
            offset_x = 0

    screen.fill((255, 255, 255))
    for layer in tmx_data.visible_layers:
        for x, y, gid in layer:
            if gid:
                tile = tmx_data.get_tile_image_by_gid(gid)
                screen.blit(tile, (x * tmx_data.tilewidth - offset_x, y * tmx_data.tileheight))

    pygame.display.flip()

pygame.quit()
sys.exit()

