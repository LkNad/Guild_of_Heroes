from const import *


def fon_win(screen, total_time):
    font = pygame.font.Font("DreiFraktur.ttf", 50)
    text = font.render('Уровень пройден', True, (255,255,255))
    fon_surface = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
    fon_surface.fill((67, 255, 86, 40))
    rect = text.get_rect()
    rect.center = (WIDTH // 2, HEIGHT // 2)
    fon_surface.blit(text, rect.topleft)

    font = pygame.font.Font("DreiFraktur.ttf", 34)
    text1 = font.render(f"Итоговое время: {total_time} сек", True,
                       (162, 219, 176))
    rect2 = text1.get_rect()
    rect2.center = (WIDTH // 2, HEIGHT // 2)
    screen.blit(text1, rect2.bottomleft)

    return fon_surface


def win(screen, time=0):
    win_sound = pygame.mixer.Sound('win_music.mp3')
    win_sound2 = pygame.mixer.Sound('ura-pobeda.mp3')
    fon = fon_win(screen, time)
    screen.blit(fon, (0, 0))
    win_sound.play()
    win_sound2.play()
    clock = pygame.time.Clock()
    running = True
    while running:
        pygame.display.flip()
        clock.tick(FPS)

def fon_hurt(screen):
    fon_surface = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
    fon_surface.fill((255, 51, 51, 40))
    return fon_surface


def hurt(screen):
    win_sound = pygame.mixer.Sound('classic_hurt.mp3')
    fon = fon_hurt(screen)
    screen.blit(fon, (0, 0))
    win_sound.play()
    clock = pygame.time.Clock()
    running = True
    while running:
        pygame.display.flip()
        clock.tick(FPS)
