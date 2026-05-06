import pygame

class Explosion(pygame.sprite.Sprite):
    def __init__(self, x, y, frames):
        super().__init__()
        self.frames = frames
        self.current_frame = 0
        self.image = self.frames[0]
        self.rect = self.image.get_rect(center = (x, y))
        self.animation_speed = 0.2

    def update(self):
        self.current_frame += self.animation_speed

        if self.current_frame < len(self.frames):
            self.image = self.frames[int(self.current_frame)]
        else:
            self.kill()