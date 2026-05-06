import pygame
import settings

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(settings.ENEMY_IMAGE_PATH).convert_alpha()
        self.image = pygame.transform.scale(
            self.image, 
            (int(self.image.get_width()*0.75), int(self.image.get_height()*0.75))
        )

        self.rect = self.image.get_rect(
            center=(settings.SCREEN_WIDTH // 2, 50)
        )

        self.step_size = 5          # velikost jednoho kroku
        self.horizontal_steps = 80  # počet kroků doprava/doleva
        self.steps_taken = 0        # kolik horizontálních kroků už udělal
        self.moving_right = True    # aktuální horizontální směr

    def update(self):
        # horizontální pohyb
        if self.steps_taken < self.horizontal_steps:
            if self.moving_right:
                self.rect.x += self.step_size
            else:
                self.rect.x -= self.step_size
            self.steps_taken += 1
        else:
            # posun dolů a přepnutí směru
            self.rect.y += self.step_size
            self.steps_taken = 0
            self.moving_right = not self.moving_right