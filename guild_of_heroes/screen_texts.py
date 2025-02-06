from const import *


def fon_win(screen):
    font = pygame.font.Font("DreiFraktur.ttf", 200)
    text = font.render('Уровень пройден', True, (125, 125, 125))
    fon_surface = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
    fon_surface.fill((67, 255, 86, 40))
    rect = text.get_rect()
    rect.center = (WIDTH // 2, HEIGHT // 2)
    fon_surface.blit(text, rect.topleft)
    return fon_surface


def win(screen):
    win_sound = pygame.mixer.Sound('data\\sound\\win.wav')
    fon = fon_win(screen)
    screen.blit(fon, (0, 0))
    win_sound.play()
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'exit'
            if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                return 'menu'
        pygame.display.flip()
        clock.tick(FPS)
