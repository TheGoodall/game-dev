import pygame


class spritesheet():
    def __init__(self, image_path: str) -> None:
        self.sheet = pygame.image.load(image_path)
    
    def get_image(self, x, y, x_size, y_size):
        image = pygame.Surface((x_size, y_size), pygame.SRCALPHA, 32).convert_alpha()
        image.blit(self.sheet, (0,0), pygame.Rect(x, y, x_size, y_size))
        return image

    def get_images(self, x, y):
        y = 4 * y
        x = 3 * x
        down =     [self.get_image((x+i)*48, y*48, 48, 48) for i in range(3)]
        left =     [self.get_image((x+i)*48, (y+1)*48, 48, 48) for i in range(3)]
        right =    [self.get_image((x+i)*48, (y+2)*48, 48, 48) for i in range(3)]
        up =       [self.get_image((x+i)*48, (y+3)*48, 48, 48) for i in range(3)]
        return [up, right, down, left]

