import pygame
import sys
# from vstuplenie import run_menu_for_back_choose

# Инициализация Pygame
pygame.init()

# Настройки экрана
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Guild of Heroes")

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
WHITE_BLUE = (214, 240, 255)

font = pygame.font.Font("DreiFraktur.ttf", 36)

background_image_characters = pygame.image.load("fon_characters.jpg")
background_image_characters = pygame.transform.scale(background_image_characters, (WIDTH, HEIGHT))
background_image_characters_2 = pygame.image.load("fon_characters_2.jpg")
background_image_characters_2 = pygame.transform.scale(background_image_characters_2, (WIDTH, HEIGHT))

# Загружаем изображения гербов
emblem1_image = pygame.image.load("gerb_1.png")
emblem2_image = pygame.image.load("gerb_2.png")
emblem3_image = pygame.image.load("gerb_3.png")
# Для проверки на пересечение
emblem1_rect = emblem1_image.get_rect()
emblem1_rect.topleft = (72, 178)
emblem2_rect = emblem1_image.get_rect()
emblem2_rect.topleft = (304, 222)
emblem3_rect = emblem1_image.get_rect()
emblem3_rect.topleft = (550, 170)
# Загружаем изображения персонажей
character1_image = pygame.image.load("1_character_choose.png")
character2_image = pygame.image.load("2_character_choose.png")
character3_image = pygame.image.load("3_character_choose.png")
character4_image = pygame.image.load("4_character_choose.png")
character5_image = pygame.image.load("5_character_choose.png")
character6_image = pygame.image.load("6_character_choose.png")
character7_image = pygame.image.load("7_character_choose.png")
character8_image = pygame.image.load("8_character_choose.png")
character9_image = pygame.image.load("9_character_choose.png")
# Для проверки на пересечение
character1_rect = character1_image.get_rect()
character1_rect.topleft = (72, 178)
character2_rect = character2_image.get_rect()
character2_rect.topleft = (341, 172)
character3_rect = character3_image.get_rect()
character3_rect.topleft = (550, 170)
character4_rect = character4_image.get_rect()
character4_rect.topleft = (72, 178)
character5_rect = character5_image.get_rect()
character5_rect.topleft = (338, 163)
character6_rect = character6_image.get_rect()
character6_rect.topleft = (550, 170)
character7_rect = character7_image.get_rect()
character7_rect.topleft = (72, 178)
character8_rect = character8_image.get_rect()
character8_rect.topleft = (328, 213)
character9_rect = character9_image.get_rect()
character9_rect.topleft = (524, 108)
# Кнопка
button_back_image = pygame.image.load("btn_back.png")
# Для проверки на пересечение
button_back_rect = button_back_image.get_rect()
button_back_rect.topleft = (31, 26)
# Кнопка2
button_back2_image = pygame.image.load("btn_back.png")
# Для проверки на пересечение
button_back2_rect = button_back2_image.get_rect()
button_back2_rect.topleft = (31, 26)

ramka_image = pygame.image.load("ramka.png")
ramka_rect = ramka_image.get_rect()
ramka_rect.topleft = (199, 467)


def draw_emblems():
    screen.blit(button_back2_image, button_back2_rect.topleft)

    screen.blit(background_image_characters, (0, 0))
    screen.blit(emblem1_image, emblem1_rect.topleft)
    screen.blit(emblem2_image, emblem2_rect.topleft)
    screen.blit(emblem3_image, emblem3_rect.topleft)

    font = pygame.font.Font("DreiFraktur.ttf", 27)
    text_surface_wars = font.render('Войны', True, WHITE)
    text_rect_wars = text_surface_wars.get_rect(topleft=(97, 424))
    text_surface_magicians = font.render('Волшебники', True, WHITE)
    text_rect_magicians = text_surface_magicians.get_rect(topleft=(302, 424))
    text_surface_fighters = font.render('Бойцы', True, WHITE)
    text_rect_fighters = text_surface_fighters.get_rect(topleft=(597, 424))

    screen.blit(text_surface_wars, text_rect_wars)
    screen.blit(text_surface_magicians, text_rect_magicians)
    screen.blit(text_surface_fighters, text_rect_fighters)


def show_wars_class():
    screen.blit(background_image_characters_2, (0, 0))
    screen.blit(character1_image, character1_rect.topleft)
    font = pygame.font.Font("DreiFraktur.ttf", 25)
    text_surface_level1 = font.render('Фрат Роп', True, WHITE_BLUE)
    text_rect_level1 = text_surface_level1.get_rect(topleft=(79, 430))
    screen.blit(text_surface_level1, text_rect_level1)
    screen.blit(character2_image, character2_rect.topleft)
    font = pygame.font.Font("DreiFraktur.ttf", 25)
    text_surface_level1 = font.render('Икари Талаф', True, WHITE_BLUE)
    text_rect_level1 = text_surface_level1.get_rect(topleft=(303, 425))
    screen.blit(text_surface_level1, text_rect_level1)
    screen.blit(character3_image, character3_rect.topleft)
    font = pygame.font.Font("DreiFraktur.ttf", 25)
    text_surface_level1 = font.render('Фодель Дотск', True, WHITE_BLUE)
    text_rect_level1 = text_surface_level1.get_rect(topleft=(545, 422))
    screen.blit(text_surface_level1, text_rect_level1)
    screen.blit(button_back_image, button_back_rect.topleft)
    font = pygame.font.Font("DreiFraktur.ttf", 20)
    text_surface_level1 = font.render('4 уровень', True, WHITE)
    text_rect_level1 = text_surface_level1.get_rect(topleft=(85, 116))
    screen.blit(text_surface_level1, text_rect_level1)
    font = pygame.font.Font("DreiFraktur.ttf", 20)
    text_surface_level2 = font.render('5 уровень', True, WHITE)
    text_rect_level2 = text_surface_level2.get_rect(topleft=(319, 119))
    screen.blit(text_surface_level2, text_rect_level2)
    font = pygame.font.Font("DreiFraktur.ttf", 20)
    text_surface_level3 = font.render('6 уровень', True, WHITE)
    text_rect_level3 = text_surface_level3.get_rect(topleft=(556, 107))
    screen.blit(text_surface_level3, text_rect_level3)
    screen.blit(ramka_image, ramka_rect.topleft)
    font = pygame.font.Font("DreiFraktur.ttf", 25)
    text_surface_ramka = font.render('Откроются позже', True, BLACK)
    text_rect_ramka = text_surface_ramka.get_rect(topleft=(228, 501))
    screen.blit(text_surface_ramka, text_rect_ramka)



def show_magicians_class():
    screen.blit(background_image_characters_2, (0, 0))
    screen.blit(character4_image, character4_rect.topleft)
    font = pygame.font.Font("DreiFraktur.ttf", 25)
    text_surface_level1 = font.render('Цефлай Халио', True, WHITE_BLUE)
    text_rect_level1 = text_surface_level1.get_rect(topleft=(59, 430))
    screen.blit(text_surface_level1, text_rect_level1)
    screen.blit(character5_image, character5_rect.topleft)
    font = pygame.font.Font("DreiFraktur.ttf", 25)
    text_surface_level1 = font.render('Витглен Граш', True, WHITE_BLUE)
    text_rect_level1 = text_surface_level1.get_rect(topleft=(303, 425))
    screen.blit(text_surface_level1, text_rect_level1)
    screen.blit(character6_image, character6_rect.topleft)
    font = pygame.font.Font("DreiFraktur.ttf", 25)
    text_surface_level1 = font.render('Кронхад Айронфут', True, WHITE_BLUE)
    text_rect_level1 = text_surface_level1.get_rect(topleft=(527, 422))
    screen.blit(text_surface_level1, text_rect_level1)
    screen.blit(button_back_image, button_back_rect.topleft)
    font = pygame.font.Font("DreiFraktur.ttf", 20)
    text_surface_level1 = font.render('7 уровень', True, WHITE)
    text_rect_level1 = text_surface_level1.get_rect(topleft=(85, 116))
    screen.blit(text_surface_level1, text_rect_level1)
    font = pygame.font.Font("DreiFraktur.ttf", 20)
    text_surface_level2 = font.render('8 уровень', True, WHITE)
    text_rect_level2 = text_surface_level2.get_rect(topleft=(319, 119))
    screen.blit(text_surface_level2, text_rect_level2)
    font = pygame.font.Font("DreiFraktur.ttf", 20)
    text_surface_level3 = font.render('9 уровень', True, WHITE)
    text_rect_level3 = text_surface_level3.get_rect(topleft=(556, 107))
    screen.blit(text_surface_level3, text_rect_level3)
    screen.blit(ramka_image, ramka_rect.topleft)
    font = pygame.font.Font("DreiFraktur.ttf", 25)
    text_surface_ramka = font.render('Откроются позже', True, BLACK)
    text_rect_ramka = text_surface_ramka.get_rect(topleft=(228, 501))
    screen.blit(text_surface_ramka, text_rect_ramka)



def show_fighters_class():
    screen.blit(background_image_characters_2, (0, 0))
    screen.blit(character7_image, character7_rect.topleft)
    font = pygame.font.Font("DreiFraktur.ttf", 25)
    text_surface_level1 = font.render('Дорн Эвенвуд', True, WHITE_BLUE)
    text_rect_level1 = text_surface_level1.get_rect(topleft=(59, 430))
    screen.blit(text_surface_level1, text_rect_level1)
    screen.blit(character8_image, character8_rect.topleft)
    font = pygame.font.Font("DreiFraktur.ttf", 25)
    text_surface_level1 = font.render('Майло Элдерберри', True, WHITE_BLUE)
    text_rect_level1 = text_surface_level1.get_rect(topleft=(303, 425))
    screen.blit(text_surface_level1, text_rect_level1)
    screen.blit(character9_image, character9_rect.topleft)
    font = pygame.font.Font("DreiFraktur.ttf", 25)
    text_surface_level1 = font.render('Фенг', True, WHITE_BLUE)
    text_rect_level1 = text_surface_level1.get_rect(topleft=(619, 447))
    screen.blit(text_surface_level1, text_rect_level1)
    screen.blit(button_back_image, button_back_rect.topleft)
    font = pygame.font.Font("DreiFraktur.ttf", 20)
    text_surface_level1 = font.render('1 уровень', True, WHITE)
    text_rect_level1 = text_surface_level1.get_rect(topleft=(85, 116))
    screen.blit(text_surface_level1, text_rect_level1)
    font = pygame.font.Font("DreiFraktur.ttf", 20)
    text_surface_level2 = font.render('2 уровень', True, WHITE)
    text_rect_level2 = text_surface_level2.get_rect(topleft=(319, 119))
    screen.blit(text_surface_level2, text_rect_level2)
    font = pygame.font.Font("DreiFraktur.ttf", 20)
    text_surface_level3 = font.render('3 уровень', True, WHITE)
    text_rect_level3 = text_surface_level3.get_rect(topleft=(574, 58))
    screen.blit(text_surface_level3, text_rect_level3)


def run_choose(scr):
    screen.fill(BLACK)
    draw_emblems()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if emblem1_rect.collidepoint(mouse_pos):
                    show_wars_class()
                elif emblem2_rect.collidepoint(mouse_pos):
                    show_magicians_class()
                elif emblem3_rect.collidepoint(mouse_pos):
                    show_fighters_class()
                elif button_back_rect.collidepoint(mouse_pos):
                    draw_emblems()
                # elif button_back2_rect.collidepoint(mouse_pos):
                #     run_menu_for_back_choose(screen)

                print(mouse_pos)

        # Обновляем экран
        pygame.display.flip()
    pygame.quit()
    sys.exit()
