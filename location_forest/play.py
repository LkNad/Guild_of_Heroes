import pygame
import sys

# Инициализация Pygame
pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Движущийся фон с элементами")

background_image = pygame.image.load('data/forest.jpeg')
background_image = pygame.transform.scale(background_image, (width, height))

platform_image_1 = pygame.image.load('data/rock.png')
platform_image_1 = pygame.transform.scale(platform_image_1, (250, 120))

platform_image_2 = pygame.image.load('data/rock(2).png')
platform_image_2 = pygame.transform.scale(platform_image_2, (200, 120))

platform_image_3 = pygame.image.load('data/rock(3).png')
platform_image_3 = pygame.transform.scale(platform_image_3, (180, 180))

tree_image = pygame.image.load('data/rock_tree(1).png')
tree_image = pygame.transform.scale(tree_image, (100, 200))

tree_image_2 = pygame.image.load('data/rock_tree(2).png')
tree_image_2 = pygame.transform.scale(tree_image_2, (75, 150))

bridge_image = pygame.image.load('data/bridge.png')
bridge_image = pygame.transform.scale(bridge_image, (220, 75))

# Позиции платформ и деревьев
platform_x_1 = 0
platform_y = height - 120

platform_x_2 = width - platform_image_2.get_width()

platform_x_3 = (width - platform_image_3.get_width()) // 2
platform_y_3 = height - 180

tree_x = platform_x_1 + (platform_image_1.get_width() - 100) * 1.5
tree_y = platform_y - 400

tree_x_2 = width - 300
tree_y_2 = 90

bridge_x = tree_x + 80
bridge_y = tree_y_2 + 100

offset = 0  # Переменная для смещения всей сцены
move_speed = 5

# Основной игровой цикл
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        offset += move_speed

    screen.blit(background_image, (-offset, 0))  # Рисую фон с учетом смещения

    # Если смещение превышает ширину фона, сбрасываем его
    if offset >= background_image.get_width():
        offset = 0

    # Отрисовка второго фона, когда первый выходит за пределы экрана
    if offset > 0:
        screen.blit(background_image, (width - offset, 0))

        # Отрисовка платформ и деревьев с учетом смещения
    screen.blit(platform_image_1, (platform_x_1 - offset, platform_y))
    screen.blit(platform_image_2, (platform_x_2 - offset, platform_y))
    screen.blit(platform_image_3, (platform_x_3 - offset, platform_y_3))
    screen.blit(tree_image, (tree_x - offset, tree_y))
    screen.blit(tree_image_2, (tree_x_2 - offset, tree_y_2))
    screen.blit(bridge_image, (bridge_x - offset, bridge_y))

    pygame.display.flip()
    pygame.time.Clock().tick(60)
