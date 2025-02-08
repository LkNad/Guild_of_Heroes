import pygame
from choose_character import Choose_character
import threading # чтобы открывалось новое независимое окно


width = 800
height = 600
black = (0, 0, 0)
white = (255, 255, 255)

pygame.init()
pygame.mixer.init()  # Инициализация микшера
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Guild of Heroes")
running = True
background_image = pygame.image.load("fon_menu.jpg")
background_image = pygame.transform.scale(background_image, (width, height))
button1 = pygame.Rect(70, 100, 260, 41)
button2 = pygame.Rect(70, 160, 260, 40)
button3 = pygame.Rect(70, 220, 260, 40)



def run_menu(scr):
    pygame.mixer.music.load("Ready_for_Action.mp3")
    pygame.mixer.music.play(-1)  # -1 означает бесконечное воспроизведение
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if button1.collidepoint(mouse_pos):
                    show_rules()
                elif button2.collidepoint(mouse_pos):
                    choose_character()
                elif button3.collidepoint(mouse_pos):
                    show_results()


        draw_menu()

    pygame.quit()


def draw_menu():
    screen.blit(background_image, (0, 0))
    font = pygame.font.Font(None, 40)
    title_text = font.render("Меню", True, white)
    screen.blit(title_text, (width // 2 - title_text.get_width() // 2, 40))

    pygame.draw.rect(screen, white, button1)
    pygame.draw.rect(screen, white, button2)
    pygame.draw.rect(screen, white, button3)

    button1_text = font.render("Правила игры", True, black)
    button2_text = font.render("Персонажи", True, black)
    button3_text = font.render("Мои результаты", True, black)

    screen.blit(button1_text, (button1.x + 30, button1.y + 7))
    screen.blit(button2_text, (button2.x + 50, button2.y + 7))
    screen.blit(button3_text, (button3.x + 20, button3.y + 10))
    pygame.display.flip()

def show_rules():
    pass

def open_new_window_character():
    choose_character_f = Choose_character()
    choose_character_f.run_choose()


def choose_character():
    new_window_character = threading.Thread(target=open_new_window_character)
    new_window_character.start()


def show_results():
    pass
