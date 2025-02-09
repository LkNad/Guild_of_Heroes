import pygame
import sys
from menu import MenuWindow

pygame.init()

size = WIDTH, HEIGHT = 1300, 800
screen = pygame.display.set_mode(size)

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
pygame.display.set_caption("Guild of Heroes")
pygame.mixer.init()  # Инициализация микшера

background_image_ded = pygame.image.load("fon_deda.jpg")

background_image_ded = pygame.transform.scale(background_image_ded, (WIDTH, HEIGHT))
pygame.mixer.music.load("vstuplenie_music.mp3")
pygame.mixer.music.play(-1)  # -1 означает бесконечное воспроизведение

# Функция для отображения текста
def show_fading_text(text, duration=6000):
    font = pygame.font.Font("DreiFraktur.ttf", 27)
    text_surfaces = [font.render(line, True, WHITE) for line in text]
    text_rects = [text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + i * 40)) for i, text_surface in enumerate(text_surfaces)]

    alpha = 0
    fade_in_step = 255 / (duration / 40)  # Увеличение альфа-канала
    fade_out_step = 255 / (duration / 60)  # Уменьшение альфа-канала

    # Плавное появление
    while alpha < 255:
        screen.fill(BLACK)  # Очистка экрана
        alpha += fade_in_step
        if alpha > 255:
            alpha = 255
        for text_surface in text_surfaces:
            text_surface.set_alpha(alpha)
            screen.blit(text_surface, text_rects[text_surfaces.index(text_surface)])
        pygame.display.flip()
        pygame.time.delay(20)

    # Плавное затухание
    while alpha > 0:
        screen.fill(BLACK)
        alpha -= fade_out_step
        if alpha < 0:
            alpha = 0
        for text_surface in text_surfaces:
            text_surface.set_alpha(alpha)
            screen.blit(text_surface, text_rects[text_surfaces.index(text_surface)])
        pygame.display.flip()
        pygame.time.delay(20)

def show_text(text):
    font = pygame.font.Font("DreiFraktur.ttf", 27)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 100))
    screen.blit(text_surface, text_rect)

screen.fill(BLACK)

show_fading_text(["Добро пожаловать в", "Guild of Heroes"])
show_fading_text(["Мы ребята из Яндекс лицея", "создали эту игру для развлечения,", "отдыха от повседневных забот", "и погружения в атмосферу нашей игры"])
show_fading_text(["Сейчас старейшина Гилдртс", "объяснит правила игры"])

font = pygame.font.Font("DreiFraktur.ttf", 24)

class Elder:
    def __init__(self, image_path, text):
        screen.blit(background_image_ded, (0, 0))
        self.image = pygame.image.load(image_path)
        self.text = text

    def draw(self, surface):
        surface.blit(self.image, (63, 260))
        text_surface = font.render(self.text, True, WHITE)
        surface.blit(text_surface, (134, 168))

def run_elder():
    global phrases
    phrases = [
        Elder("gildrts_2.png", "Привет, новый герой!"),
        Elder("gildrts_1.png", "Тебя ждет великая игра."),
        Elder("gildrts_2.png", "Стань отважным героем."),
        Elder("gildrts_2.png", "Пройди через множество испытаний."),
        Elder("gildrts_2.png", "Сразись с ужасными монстрами."),
        Elder("gildrts_2.png", "Спаси нашу деревню!"),
        Elder("gildrts_1.png", "В каждом уровне специальные задания"),
        Elder("gildrts_2.png", "А на пути встретятся разные чудовища"),
        Elder("gildrts_1.png", "Выполняй уровни и убивай монстров"),
        Elder("gildrts_1.png", "Проходи уровень быстрее!"),
        Elder("gildrts_2.png", "Будьте готовы к сражениям!"),
        Elder("gildrts_2.png", "Используйте навыки и ловкость."),
        Elder("gildrts_2.png", "Каждый уровень сложнее предыдущего."),
        Elder("gildrts_1.png", "Но смелость - ключ к успеху."),
        Elder("gildrts_2.png", "Вперед, к приключениям!"),
        Elder("gildrts_2.png", "Станьте легендой!"),
    ]

run_elder()

def run_intro():
    current_phrase_index = 0
    clock = pygame.time.Clock()
    end_of_phrases = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                current_phrase_index += 1
                if current_phrase_index >= len(phrases):
                    end_of_phrases = True

        # Отрисовка
        if not end_of_phrases:
            screen.blit(background_image_ded, (0, 0))
            phrases[current_phrase_index].draw(screen)
        else:
            # Переход к меню
            menu = MenuWindow()
            menu.run()  # Запускаем меню
            pygame.quit()  # Завершение работы Pygame после выхода из меню
            sys.exit()

        # Обновление экрана
        pygame.display.flip()
        clock.tick(60)

run_intro()
