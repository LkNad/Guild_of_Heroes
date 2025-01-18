import pygame

width = 1000
height = 500
black = (0, 0, 0)
white = (255, 255, 255)


class MenuWindow:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Меню")
        self.running = True
        self.background_image = pygame.image.load("фон.jpg")
        self.background_image = pygame.transform.scale(self.background_image, (width, height))
        self.button1 = pygame.Rect(70, 100, 260, 40)
        self.button2 = pygame.Rect(70, 160, 260, 40)
        self.button3 = pygame.Rect(70, 220, 260, 40)

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if self.button1.collidepoint(mouse_pos):
                        self.show_rules()
                    elif self.button2.collidepoint(mouse_pos):
                        self.choose_character()
                    elif self.button3.collidepoint(mouse_pos):
                        self.show_results()

            self.draw()

        pygame.quit()

    def draw(self):
        self.screen.blit(self.background_image, (0, 0))
        font = pygame.font.Font(None, 40)
        title_text = font.render("Меню", True, white)
        self.screen.blit(title_text, (width // 2 - title_text.get_width() // 2, 40))

        pygame.draw.rect(self.screen, white, self.button1)
        pygame.draw.rect(self.screen, white, self.button2)
        pygame.draw.rect(self.screen, white, self.button3)

        button1_text = font.render("правила игры", True, black)
        button2_text = font.render("Выбор персонажа", True, black)
        button3_text = font.render("мои результаты", True, black)

        self.screen.blit(button1_text, (self.button1.x + 30, self.button1.y + 7))
        self.screen.blit(button2_text, (self.button2.x + 5, self.button2.y + 7))
        self.screen.blit(button3_text, (self.button3.x + 20, self.button3.y + 10))
        pygame.display.flip()

    def show_rules(self):
        pass

    def choose_character(self):
        pass

    def show_results(self):
        pass


if __name__ == "__main__":
    menu = MenuWindow()
    menu.run()
