import pygame
import settings
from Player import Player


class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(settings.BULLET_IMAGE_PATH).convert_alpha()
        self.image = pygame.transform.scale(
            self.image, 
            (int(self.image.get_width()*0.75), int(self.image.get_height()*0.75))
        )

        self.rect = self.image.get_rect(
            center=(settings.SCREEN_WIDTH // 2, settings.SCREEN_HEIGHT - 20)
        )



    def update(self):
        self.rect.y -= 5
