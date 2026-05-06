import pygame
import settings
import random as rand
from Enemy_Bullet import Enemy_Bullet

class Enemy(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        alien_type = rand.randint(1,5)
        self.image = pygame.image.load(settings.ENEMY_IMAGE_PATH.format(alien_type)).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width()*settings.ENEMY_SCALE, self.image.get_height()*settings.ENEMY_SCALE))
        self.rect = self.image.get_rect(top=y, centerx=x)
        self.speed = settings.PLAYER_SPEED


        self.step_sizex = 5
        self.step_sizey = 20         
        self.horizontal_steps = 70 
        self.steps_taken = 0       
        self.moving_right = True  

    def update(self):
        # horizontální pohyb
        if self.steps_taken < self.horizontal_steps:
            if self.moving_right:
                self.rect.x += self.step_sizex
            else:
                self.rect.x -= self.step_sizex
            self.steps_taken += 1
        else:
            # posun dolů a přepnutí směru
            self.rect.y += self.step_sizey
            self.steps_taken = 0
            self.moving_right = not self.moving_right




if __name__ == "__main__":
    import main
