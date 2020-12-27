
# Import Modules
import pygame

# Import game components
import DontWaitVaccinate.events as events
import DontWaitVaccinate.loop as loop
import DontWaitVaccinate.render as render
import DontWaitVaccinate.game as game

# Initialise Pygame and displays
pygame.init()
screen = pygame.display.set_mode((480, 320), pygame.RESIZABLE)
surface = pygame.Surface((1280, 720))

# Initialise Game
game_instance = game.game()

# Main Loop
while game_instance.running:

    # Process events
    events.events(game_instance)

    # Run main game loop
    loop.loop(game_instance)

    # Render Game to surface
    render.render(surface, game_instance)

    # Scale surface and render to screen
    pygame.transform.scale(
        surface, (screen.get_width(), screen.get_height()), screen)
    pygame.display.update()
