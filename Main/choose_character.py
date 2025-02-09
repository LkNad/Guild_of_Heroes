import pygame
import sys

# Инициализация Pygame
pygame.init()

# Настройки экрана
WIDTH, HEIGHT = 800, 600

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
WHITE_BLUE = (214, 240, 255)


class Choose_character:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Guild of Heroes")
        font = pygame.font.Font("DreiFraktur.ttf", 36)

        self.background_image_characters = pygame.image.load("fon_characters.jpg")
        self.background_image_characters = pygame.transform.scale(self.background_image_characters, (WIDTH, HEIGHT))
        self.background_image_characters_2 = pygame.image.load("fon_characters_2.jpg")
        self.background_image_characters_2 = pygame.transform.scale(self.background_image_characters_2, (WIDTH, HEIGHT))

        # Загружаем изображения гербов
        self.emblem1_image = pygame.image.load("data/gerb_1.png")
        self.emblem2_image = pygame.image.load("data/gerb_2.png")
        self.emblem3_image = pygame.image.load("data/gerb_3.png")
        # Для проверки на пересечение
        self.emblem1_rect = self.emblem1_image.get_rect()
        self.emblem1_rect.topleft = (72, 178)
        self.emblem2_rect = self.emblem1_image.get_rect()
        self.emblem2_rect.topleft = (304, 222)
        self.emblem3_rect = self.emblem1_image.get_rect()
        self.emblem3_rect.topleft = (550, 170)
        # Загружаем изображения персонажей
        self.character1_image = pygame.image.load("data/1_character_choose.png")
        self.character2_image = pygame.image.load("data/2_character_choose.png")
        self.character3_image = pygame.image.load("data/3_character_choose.png")
        self.character4_image = pygame.image.load("data/4_character_choose.png")
        self.character5_image = pygame.image.load("data/5_character_choose.png")
        self.character6_image = pygame.image.load("data/6_character_choose.png")
        self.character7_image = pygame.image.load("data/7_character_choose.png")
        self.character8_image = pygame.image.load("data/8_character_choose.png")
        self.character9_image = pygame.image.load("data/9_character_choose.png")
        # Для проверки на пересечение
        self.character1_rect = self.character1_image.get_rect()
        self.character1_rect.topleft = (72, 178)
        self.character2_rect = self.character2_image.get_rect()
        self.character2_rect.topleft = (341, 172)
        self.character3_rect = self.character3_image.get_rect()
        self.character3_rect.topleft = (550, 170)
        self.character4_rect = self.character4_image.get_rect()
        self.character4_rect.topleft = (72, 178)
        self.character5_rect = self.character5_image.get_rect()
        self.character5_rect.topleft = (338, 163)
        self.character6_rect = self.character6_image.get_rect()
        self.character6_rect.topleft = (550, 170)
        self.character7_rect = self.character7_image.get_rect()
        self.character7_rect.topleft = (72, 178)
        self.character8_rect = self.character8_image.get_rect()
        self.character8_rect.topleft = (328, 213)
        self.character9_rect = self.character9_image.get_rect()
        self.character9_rect.topleft = (524, 108)
        # Кнопка
        self.button_back_image = pygame.image.load("data/btn_back.png")
        # Для проверки на пересечение
        self.button_back_rect = self.button_back_image.get_rect()
        self.button_back_rect.topleft = (31, 26)
        # Кнопка2
        self.button_back2_image = pygame.image.load("data/btn_back.png")
        # Для проверки на пересечение
        self.button_back2_rect = self.button_back2_image.get_rect()
        self.button_back2_rect.topleft = (31, 26)

        self.ramka_image = pygame.image.load("data/ramka.png")
        self.ramka_rect = self.ramka_image.get_rect()
        self.ramka_rect.topleft = (199, 467)

    def draw_emblems(self):
        self.screen.blit(self.button_back2_image, self.button_back2_rect.topleft)

        self.screen.blit(self.background_image_characters, (0, 0))
        self.screen.blit(self.emblem1_image, self.emblem1_rect.topleft)
        self.screen.blit(self.emblem2_image, self.emblem2_rect.topleft)
        self.screen.blit(self.emblem3_image, self.emblem3_rect.topleft)

        font = pygame.font.Font("DreiFraktur.ttf", 27)
        self.text_surface_wars = font.render('Войны', True, WHITE)
        self.text_rect_wars = self.text_surface_wars.get_rect(topleft=(97, 424))
        self.text_surface_magicians = font.render('Волшебники', True, WHITE)
        self.text_rect_magicians = self.text_surface_magicians.get_rect(topleft=(302, 424))
        self.text_surface_fighters = font.render('Бойцы', True, WHITE)
        self.text_rect_fighters = self.text_surface_fighters.get_rect(topleft=(597, 424))

        self.screen.blit(self.text_surface_wars, self.text_rect_wars)
        self.screen.blit(self.text_surface_magicians, self.text_rect_magicians)
        self.screen.blit(self.text_surface_fighters, self.text_rect_fighters)

    def show_wars_class(self):
        self.screen.blit(self.background_image_characters_2, (0, 0))
        self.screen.blit(self.character1_image, self.character1_rect.topleft)

        font = pygame.font.Font("DreiFraktur.ttf", 25)
        self.text_surface_level1 = font.render('Фрат Роп', True, WHITE_BLUE)
        self.text_rect_level1 = self.text_surface_level1.get_rect(topleft=(79, 430))
        self.screen.blit(self.text_surface_level1, self.text_rect_level1)
        self.screen.blit(self.character2_image, self.character2_rect.topleft)
        font = pygame.font.Font("DreiFraktur.ttf", 25)
        text_surface_level1 = font.render('Икари Талаф', True, WHITE_BLUE)
        text_rect_level1 = text_surface_level1.get_rect(topleft=(303, 425))
        self.screen.blit(text_surface_level1, text_rect_level1)
        self.screen.blit(self.character3_image, self.character3_rect.topleft)
        font = pygame.font.Font("DreiFraktur.ttf", 25)
        text_surface_level1 = font.render('Фодель Дотск', True, WHITE_BLUE)
        text_rect_level1 = text_surface_level1.get_rect(topleft=(545, 422))
        self.screen.blit(text_surface_level1, text_rect_level1)
        self.screen.blit(self.button_back_image, self.button_back_rect.topleft)
        font = pygame.font.Font("DreiFraktur.ttf", 20)
        text_surface_level1 = font.render('4 уровень', True, WHITE)
        text_rect_level1 = text_surface_level1.get_rect(topleft=(85, 116))
        self.screen.blit(text_surface_level1, text_rect_level1)
        font = pygame.font.Font("DreiFraktur.ttf", 20)
        text_surface_level2 = font.render('5 уровень', True, WHITE)
        text_rect_level2 = text_surface_level2.get_rect(topleft=(319, 119))
        self.screen.blit(text_surface_level2, text_rect_level2)
        font = pygame.font.Font("DreiFraktur.ttf", 20)
        text_surface_level3 = font.render('6 уровень', True, WHITE)
        text_rect_level3 = text_surface_level3.get_rect(topleft=(556, 107))
        self.screen.blit(text_surface_level3, text_rect_level3)
        self.screen.blit(self.ramka_image, self.ramka_rect.topleft)
        font = pygame.font.Font("DreiFraktur.ttf", 25)
        text_surface_ramka = font.render('Откроются позже', True, BLACK)
        text_rect_ramka = text_surface_ramka.get_rect(topleft=(228, 501))
        self.screen.blit(text_surface_ramka, text_rect_ramka)

    def show_magicians_class(self):
        self.screen.blit(self.background_image_characters_2, (0, 0))
        self.screen.blit(self.character4_image, self.character4_rect.topleft)
        font = pygame.font.Font("DreiFraktur.ttf", 25)
        text_surface_level1 = font.render('Цефлай Халио', True, WHITE_BLUE)
        text_rect_level1 = text_surface_level1.get_rect(topleft=(59, 430))
        self.screen.blit(text_surface_level1, text_rect_level1)
        self.screen.blit(self.character5_image, self.character5_rect.topleft)
        font = pygame.font.Font("DreiFraktur.ttf", 25)
        text_surface_level1 = font.render('Витглен Граш', True, WHITE_BLUE)
        text_rect_level1 = text_surface_level1.get_rect(topleft=(303, 425))
        self.screen.blit(text_surface_level1, text_rect_level1)
        self.screen.blit(self.character6_image, self.character6_rect.topleft)
        font = pygame.font.Font("DreiFraktur.ttf", 25)
        text_surface_level1 = font.render('Кронхад Айронфут', True, WHITE_BLUE)
        text_rect_level1 = text_surface_level1.get_rect(topleft=(527, 422))
        self.screen.blit(text_surface_level1, text_rect_level1)
        self.screen.blit(self.button_back_image, self.button_back_rect.topleft)
        font = pygame.font.Font("DreiFraktur.ttf", 20)
        text_surface_level1 = font.render('7 уровень', True, WHITE)
        text_rect_level1 = text_surface_level1.get_rect(topleft=(85, 116))
        self.screen.blit(text_surface_level1, text_rect_level1)
        font = pygame.font.Font("DreiFraktur.ttf", 20)
        text_surface_level2 = font.render('8 уровень', True, WHITE)
        text_rect_level2 = text_surface_level2.get_rect(topleft=(319, 119))
        self.screen.blit(text_surface_level2, text_rect_level2)
        font = pygame.font.Font("DreiFraktur.ttf", 20)
        text_surface_level3 = font.render('9 уровень', True, WHITE)
        text_rect_level3 = text_surface_level3.get_rect(topleft=(556, 107))
        self.screen.blit(text_surface_level3, text_rect_level3)
        self.screen.blit(self.ramka_image, self.ramka_rect.topleft)
        font = pygame.font.Font("DreiFraktur.ttf", 25)
        text_surface_ramka = font.render('Откроются позже', True, BLACK)
        text_rect_ramka = text_surface_ramka.get_rect(topleft=(228, 501))
        self.screen.blit(text_surface_ramka, text_rect_ramka)

    def show_fighters_class(self):
        self.screen.blit(self.background_image_characters_2, (0, 0))
        self.screen.blit(self.character7_image, self.character7_rect.topleft)
        font = pygame.font.Font("DreiFraktur.ttf", 25)
        text_surface_level1 = font.render('Дорн Эвенвуд', True, WHITE_BLUE)
        text_rect_level1 = text_surface_level1.get_rect(topleft=(59, 430))
        self.screen.blit(text_surface_level1, text_rect_level1)
        self.screen.blit(self.character8_image, self.character8_rect.topleft)
        font = pygame.font.Font("DreiFraktur.ttf", 25)
        text_surface_level1 = font.render('Майло Элдерберри', True, WHITE_BLUE)
        text_rect_level1 = text_surface_level1.get_rect(topleft=(303, 425))
        self.screen.blit(text_surface_level1, text_rect_level1)
        self.screen.blit(self.character9_image, self.character9_rect.topleft)
        font = pygame.font.Font("DreiFraktur.ttf", 25)
        text_surface_level1 = font.render('Фенг', True, WHITE_BLUE)
        text_rect_level1 = text_surface_level1.get_rect(topleft=(619, 447))
        self.screen.blit(text_surface_level1, text_rect_level1)
        self.screen.blit(self.button_back_image, self.button_back_rect.topleft)
        font = pygame.font.Font("DreiFraktur.ttf", 20)
        text_surface_level1 = font.render('1 уровень', True, WHITE)
        text_rect_level1 = text_surface_level1.get_rect(topleft=(85, 116))
        self.screen.blit(text_surface_level1, text_rect_level1)
        font = pygame.font.Font("DreiFraktur.ttf", 20)
        text_surface_level2 = font.render('2 уровень', True, WHITE)
        text_rect_level2 = text_surface_level2.get_rect(topleft=(319, 119))
        self.screen.blit(text_surface_level2, text_rect_level2)
        font = pygame.font.Font("DreiFraktur.ttf", 20)
        text_surface_level3 = font.render('3 уровень', True, WHITE)
        text_rect_level3 = text_surface_level3.get_rect(topleft=(574, 58))
        self.screen.blit(text_surface_level3, text_rect_level3)

    def run_choose(self):
        self.screen.fill(BLACK)
        self.draw_emblems()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if self.emblem1_rect.collidepoint(mouse_pos):
                        self.show_wars_class()
                    elif self.emblem2_rect.collidepoint(mouse_pos):
                        self.show_magicians_class()
                    elif self.emblem3_rect.collidepoint(mouse_pos):
                        self.show_fighters_class()
                    elif self.button_back_rect.collidepoint(mouse_pos):
                        self.draw_emblems()


            # Обновляем экран
            pygame.display.flip()
        pygame.quit()
        sys.exit()



