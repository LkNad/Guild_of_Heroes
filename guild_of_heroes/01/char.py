import pygame
import sys

class Game:
    def __init__(self):
        pygame.init()
        self.WIDTH, self.HEIGHT = 1300, 800
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Персонажи")

        self.character_images = [
            pygame.image.load("1_character_choose.png"),
            pygame.image.load("2_character_choose.png"),
            pygame.image.load("3_character_choose.png"),
            pygame.image.load("4_character_choose.png"),
            pygame.image.load("5_character_choose.png"),
            pygame.image.load("6_character_choose.png"),
        ]

        self.background_image = pygame.image.load("fon_menu.jpg")
        self.background_image = pygame.transform.scale(self.background_image, (self.WIDTH, self.HEIGHT))

        self.current_character = 0
        self.character_rect = self.character_images[self.current_character].get_rect(center=(self.WIDTH // 2, self.HEIGHT // 2))

        self.WHITE = (255, 255, 255)
        self.BUTTON_COLOR = (100, 100, 255)
        self.TEXT_COLOR = (0, 0, 0)
        self.FLOOR_COLOR = (150, 75, 0)

        self.left_button_rect = pygame.Rect(50, self.HEIGHT // 2 - 25, 50, 50)
        self.right_button_rect = pygame.Rect(self.WIDTH - 100, self.HEIGHT // 2 - 25, 50, 50)
        self.exit_button_rect = pygame.Rect(self.WIDTH // 2 - 75, self.HEIGHT - 60, 150, 50)  # Кнопка "Выйти"

        self.font = pygame.font.Font(None, 36)

    def show(self):
        self.run()

    def run(self):
        while True:
            self.handle_events()
            self.update()
            self.draw()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.current_character = (self.current_character + 1) % len(self.character_images)
                elif event.key == pygame.K_LEFT:
                    self.current_character = (self.current_character - 1) % len(self.character_images)

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if self.left_button_rect.collidepoint(mouse_pos):
                    self.current_character = (self.current_character - 1) % len(self.character_images)
                elif self.right_button_rect.collidepoint(mouse_pos):
                    self.current_character = (self.current_character + 1) % len(self.character_images)
                elif self.exit_button_rect.collidepoint(mouse_pos):  # Проверка нажатия на кнопку "Выйти"
                    self.quit_to_menu()

    def update(self):
        self.character_rect = self.character_images[self.current_character].get_rect(center=(self.WIDTH // 2, self.HEIGHT // 2))

    def draw(self):
        self.screen.blit(self.background_image, (0, 0))
        self.screen.blit(self.character_images[self.current_character], self.character_rect)

        floor_rect = pygame.Rect(self.character_rect.x, self.character_rect.bottom, self.character_rect.width, 10)
        pygame.draw.rect(self.screen, self.FLOOR_COLOR, floor_rect)

        pygame.draw.rect(self.screen, self.BUTTON_COLOR, self.left_button_rect)
        pygame.draw.rect(self.screen, self.BUTTON_COLOR, self.right_button_rect)
        pygame.draw.rect(self.screen, self.BUTTON_COLOR, self.exit_button_rect)  # Рисуем кнопку "Выйти"

        left_arrow = self.font.render("<", True, self.WHITE)
        right_arrow = self.font.render(">", True, self.WHITE)
        self.screen.blit(left_arrow, (self.left_button_rect.x + 10, self.left_button_rect.y + 5))
        self.screen.blit(right_arrow, (self.right_button_rect.x + 10, self.right_button_rect.y + 5))

        exit_text = self.font.render("Выйти", True, self.WHITE)
        # Отрисовка текста на кнопке "Выйти"
        self.screen.blit(exit_text, (self.exit_button_rect.x + (self.exit_button_rect.width - exit_text.get_width()) // 2,
                                      self.exit_button_rect.y + (self.exit_button_rect.height - exit_text.get_height()) // 2))

        update_text = self.font.render("Совсем скоро...", True, self.TEXT_COLOR)
        self.screen.blit(update_text, (self.WIDTH // 2 - update_text.get_width() // 2, 20))
        update_text_2 = self.font.render("В следующем обновлении игры", True, self.TEXT_COLOR)
        self.screen.blit(update_text_2, (self.WIDTH // 2 - update_text_2.get_width() // 2, 50))

        pygame.display.flip()

    def quit_to_menu(self):
        # Здесь можно добавить код для возврата в меню
        from menu import MenuWindow
        menu_window = MenuWindow()
        menu_window.run()

        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = Game()
    game.run()
