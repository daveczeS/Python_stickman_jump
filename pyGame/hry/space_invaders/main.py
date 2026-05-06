import pygame
import settings
from Player import Player # Tvůj hráč
from Enemy import Enemy
from Bullet import Bullet
pygame.init()

screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
pygame.display.set_caption("Space Invaders")

running = True
state = "MENU"   # MENU, COUNTDOWN, PLAYING, SETTINGS, GAME_OVER

# --- font pro odpočet ---
countdown_font = pygame.font.Font(None, 120)
countdown_start = 0

# --- hráč ---
player_group = pygame.sprite.Group()
player = None

enemy_group = pygame.sprite.Group()
enemy = None

bullet_group = pygame.sprite.Group()
bullet = None

# --- Funkce pro vykreslení menu ---
def vypis_menu():
    screen.fill((0, 0, 127))
    screen.blit(settings.title_text, settings.title_rect)
    screen.blit(settings.play_text, settings.play_rect)
    screen.blit(settings.settings_text, settings.settings_rect)
    screen.blit(settings.quit_text, settings.quit_rect)

def vypis_settings():
    screen.fill((0, 0, 127))
    screen.blit(settings.res800_text, settings.res800_rect)
    screen.blit(settings.res1024_text, settings.res1024_rect)
    screen.blit(settings.res1280_text, settings.res1280_rect)
    screen.blit(settings.back_text, settings.back_rect)

# --- Hlavní loop ---
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if state == "MENU":
                if settings.play_rect.collidepoint(event.pos):
                    state = "COUNTDOWN"
                    countdown_start = pygame.time.get_ticks()

                elif settings.settings_rect.collidepoint(event.pos):
                    state = "SETTINGS"

                elif settings.quit_rect.collidepoint(event.pos):
                    running = False

            elif state == "SETTINGS":
                if settings.res800_rect.collidepoint(event.pos):
                    settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT = 800, 600
                    screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
                    settings.update_rects()

                elif settings.res1024_rect.collidepoint(event.pos):
                    settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT = 1024, 768
                    screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
                    settings.update_rects()

                elif settings.res1280_rect.collidepoint(event.pos):
                    settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT = 1280, 960
                    screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
                    settings.update_rects()

                elif settings.back_rect.collidepoint(event.pos):
                    state = "MENU"

    # --- vykreslování ---
    if state == "MENU":
        vypis_menu()

    elif state == "COUNTDOWN":
        screen.fill((0, 0, 0))
        elapsed = (pygame.time.get_ticks() - countdown_start) // 1000
        if elapsed < 3:
            number = 3 - elapsed
            text = countdown_font.render(str(number), True, (255, 255, 255))
            rect = text.get_rect(center=(settings.SCREEN_WIDTH // 2, settings.SCREEN_HEIGHT // 2))
            screen.blit(text, rect)
        else:
            # vytvoření hráče po odpočtu
            player = Player()
            enemy = Enemy()
            enemy1 = Enemy()
            bullet = Bullet()
            player_group.empty()
            player_group.add(player)
            enemy_group.empty()
            enemy_group.add(enemy)
            enemy_group.add(enemy1)
            bullet_group.empty()
            bullet_group.add(bullet)
            state = "PLAYING"

    elif state == "PLAYING":
        screen.fill((0, 0, 0))
        player_group.update()
        player_group.draw(screen)
        enemy_group.update()
        enemy_group.draw(screen)
        bullet_group.update()
        bullet_group.draw(screen)

    elif state == "SETTINGS":
        vypis_settings()

    elif state == "GAME_OVER":
        screen.fill((0, 0, 0))

    pygame.display.flip()
    clock.tick(30)

pygame.quit()