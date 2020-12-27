import pygame


def events(game_instance):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_instance.running = False
