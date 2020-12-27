import pygame

import DontWaitVaccinate.events as events
import DontWaitVaccinate.loop as loop
import DontWaitVaccinate.render as render

pygame.init()
screen = pygame.display.set_mode((480, 320), pygame.RESIZABLE)
surface = pygame.Surface((1280, 720))
running = True

while running:
    running = events.events()
    loop.loop()
    render.render(surface)
    pygame.transform.scale(
        surface, (screen.get_width(), screen.get_height()), screen)
    pygame.display.update()
