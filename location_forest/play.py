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
platform_image_2 = pygame.transform.scale(platform_image_2, (150, 120))

platform_image_3 = pygame.image.load('data/rock(3).png')
platform_image_3 = pygame.transform.scale(platform_image_3, (180, 180))

platform_image_4 = pygame.image.load('data/rock(4).png')
platform_image_4 = pygame.transform.scale(platform_image_4, (200, 100))

rock_image_1 = pygame.image.load('data/rock(1).png')
rock_image_1 = pygame.transform.scale(rock_image_1, (210, 155))

tree_image = pygame.image.load('data/rock_tree(1).png')
tree_image = pygame.transform.scale(tree_image, (100, 200))

tree_image_2 = pygame.image.load('data/rock_tree(2).png')
tree_image_2 = pygame.transform.scale(tree_image_2, (75, 150))

tree_image_3 = pygame.image.load('data/rock_tree(3).png')
tree_image_3 = pygame.transform.scale(tree_image_3, (80, 100))

tree_image_4 = pygame.image.load('data/rock_tree(4).png')
tree_image_4 = pygame.transform.scale(tree_image_4, (90, 180))

# Загружаем изображение лестницы
ladder_image = pygame.image.load('data/ladder(1).png')
ladder_image = pygame.transform.scale(ladder_image, (50, 200))

bridge_image = pygame.image.load('data/bridge.png')
bridge_image = pygame.transform.scale(bridge_image, (220, 75))


# Класс для игровых объектов
class GameObject:
    def __init__(self, image, x, y):
        self.image = image
        self.rect = self.image.get_rect(topleft=(x, y))

    def draw(self, surface, offset):
        # Отрисовываю объект с учетом смещения
        surface.blit(self.image, (self.rect.x - offset, self.rect.y))


# Создаю список объектов
objects = [
    GameObject(platform_image_1, 0, height - 120),
    GameObject(platform_image_2, width - platform_image_2.get_width() - 50, height - 120),
    GameObject(platform_image_3, (width - platform_image_3.get_width()) // 2, height - 180),
    GameObject(platform_image_4, (width - platform_image_4.get_width()) // 2 + 525, height - 150),
    GameObject(tree_image, 0 + (platform_image_1.get_width() - 100) * 1.5, height - 520),
    GameObject(tree_image_2, width - 300, 90),
    GameObject(tree_image_3, (width - tree_image_3.get_width()) // 2 + 800, height - 450),
    GameObject(tree_image_4, (width - tree_image_4.get_width()) // 2 + 820, height - 175),
    GameObject(ladder_image, (width - ladder_image.get_width()) // 2 + 800, height - 360),
    GameObject(bridge_image, (0 + (platform_image_1.get_width() - 100) * 1.5) + 80, 90 + 100),
    GameObject(rock_image_1, width + 600, height - 120)
]

offset = 0
move_speed = 5
can_move = True  # Флаг для контроля движения

# Основной игровой цикл
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Проверка нажатия клавиш
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] and can_move:
        offset += move_speed

        # Проверка на достижение rock(2)
    if offset >= (width - platform_image_2.get_width() - 50 + platform_image_2.get_width()):
        can_move = False  # Останавливаю движение

    # Отрисовка фона с учетом смещения
    screen.blit(background_image, (-offset, 0))

    # Если смещение превышает ширину фона, сбрасываем его
    if offset >= background_image.get_width():
        offset = 0

    # Отрисовка второго фона, когда первый выходит за пределы экрана
    if offset > 0:
        screen.blit(background_image, (width - offset, 0))

        # Удаляю объекты, которые вышли за пределы экрана
    if can_move:
        objects = [obj for obj in objects if obj.rect.x - offset + obj.rect.width > 0]

    # Отрисовка оставшихся объектов
    for obj in objects:
        obj.draw(screen, offset)
    pygame.display.flip()
    pygame.time.Clock().tick(60)

# Завершение Pygame
pygame.quit()
