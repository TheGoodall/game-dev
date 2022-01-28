
# Import Modules
import pygame

# Import game component
import DontWaitVaccinate.game as game

# Initialise game constants
FRAMERATE = 60
DEFAULT_SCREEN_RES = (640, 360)
PYGAME_FLAGS = pygame.SCALED | pygame.RESIZABLE
BACKGROUND_COLOUR = (0, 0, 0)

# Initialise Pygame and displays
pygame.init()
screen = pygame.display.set_mode(DEFAULT_SCREEN_RES, PYGAME_FLAGS)

# Initialise Font
font = pygame.font.SysFont("ubuntu", 12)

# Initialise clock
clock = pygame.time.Clock()

# Initialise Game
game_instance = game.game()

# Main Loop
while game_instance.running:

    # Tick clock at 60fps
    clock.tick(FRAMERATE)
    time = clock.get_time()

    # Process events
    game_instance.loop(time)

    # Clear screen
    screen.fill(BACKGROUND_COLOUR)

    # Render Game to surface
    game_instance.render(screen, font)

    # Scale surface and render to screen
    pygame.display.update()
