import pygame

WIDTH, HEIGHT = 800, 600
FPS = 60
DAMAGE_EVENT = pygame.event.Event(pygame.USEREVENT, attr1='DAMAGE_EVENT')
GAME_OVER_EVENT = pygame.event.Event(pygame.USEREVENT, attr1='GAME_OVER_EVENT')
WIN_EVENT = pygame.event.Event(pygame.USEREVENT, attr1='WIN_EVENT')
