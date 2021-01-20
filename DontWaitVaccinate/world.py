import pygame


class World():
    """ Contains the current state of the world, e.g. buildings """

    def __init__(self, size: int, density: int) -> None:
        self.ground_texture = pygame.image.load(
            "DontWaitVaccinate/images/grass.jpg")
        self.ground_texture = pygame.transform.scale(
            self.ground_texture, (500, 500))

    def render_ground(self, surface, font, cam_pos):
        screen_size = surface.get_size()
        texture_size = self.ground_texture.get_size()
        cam_pos = round(cam_pos[0]), round(cam_pos[1])

        render_offset = -(cam_pos[0] % texture_size[0]
                          ), -(cam_pos[1] % texture_size[1])

        count = round(screen_size[0] / texture_size[0] +
                      1), round(screen_size[0] / texture_size[0] + 1)

        render = []

        for i in range(count[0]):
            for j in range(count[1]):
                render_pos = (
                    render_offset[0] + i * texture_size[0],
                    render_offset[1] + j * texture_size[1]
                )
                render.append((self.ground_texture, render_pos))

        surface.blits(render)
