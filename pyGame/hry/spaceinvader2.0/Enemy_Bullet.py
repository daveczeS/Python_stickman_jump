import pygame
import settings
from Player import Player


class Enemy_Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.image.load(settings.ENEMY_BULLET_IMAGE_PATH).convert_alpha()
        self.image = pygame.transform.scale(
            self.image, 
            (int(self.image.get_width()*0.75), int(self.image.get_height()*0.75))
        )

        self.rect = self.image.get_rect(
            center=(x,y)
        )

    

    def update(self):
        self.rect.y += 5
