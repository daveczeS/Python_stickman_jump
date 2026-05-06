import pygame
import settings
from Player import Player
from Enemy import Enemy
from Bullet import Bullet
from Enemy_Bullet import Enemy_Bullet
from Explosion import Explosion
import random as rand

pygame.init()

screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
pygame.display.set_caption("Space Invaders")

clock = pygame.time.Clock()
running = True
state = "MENU"

# --- FONTY ---
countdown_font = pygame.font.Font(None, 120)
base_font = pygame.font.Font(None, 40)
countdown_start = 0

# --- GROUPY ---
player_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()
enemy_bullet_group = pygame.sprite.Group()
explosion_group = pygame.sprite.Group()

# --- PROMĚNNÉ ---
player = None
score = 0
strelba = 0
new_score = 10
game_over = False

# --- NAČTENÍ BEST SCORE ---
try:
    with open("score.txt", "r") as s:
        best = int(s.read())
except:
    best = 0

# --- EXPLOSION IMG ---
explosion_images = []
for i in range(1, 6):
    explosion_images.append(pygame.image.load(f"img/exp{i}.png"))

# --- MENU ---
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

# --- START HRY ---
def start_game():
    global player, score, strelba, new_score, game_over

    player_group.empty()
    enemy_group.empty()
    bullet_group.empty()
    enemy_bullet_group.empty()
    explosion_group.empty()

    player = Player()
    player_group.add(player)

    x, y = 25, -100
    for j in range(2):
        x = 25
        y += 100
        for i in range(5):
            enemy_group.add(Enemy(x, y))
            x += 100

    score = 0
    strelba = 0
    new_score = 10
    game_over = False

# --- HLAVNÍ LOOP ---
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

            elif state == "PLAYING":
                if strelba <= 0:
                    bullet = Bullet(player.rect.x + 25, player.rect.y)
                    bullet_group.add(bullet)
                    strelba = 40

    # --- STAVY ---

    if state == "MENU":
        vypis_menu()

    elif state == "SETTINGS":
        vypis_settings()

    elif state == "COUNTDOWN":
        screen.fill((0, 0, 0))
        elapsed = (pygame.time.get_ticks() - countdown_start) // 1000

        if elapsed < 3:
            text = countdown_font.render(str(3 - elapsed), True, (255, 255, 255))
            rect = text.get_rect(center=(settings.SCREEN_WIDTH // 2, settings.SCREEN_HEIGHT // 2))
            screen.blit(text, rect)
        else:
            start_game()
            state = "PLAYING"

    elif state == "PLAYING":

        screen.fill(settings.BG_COLOR)

        strelba -= 1

        for e in enemy_group:
            if rand.randint(1, 100) == 25:
                enemy_bullet_group.add(Enemy_Bullet(e.rect.x + 25, e.rect.y + 25))

            # zásah hráče
            if pygame.sprite.spritecollide(player, enemy_bullet_group, True):
                player.kill()
                explosion_group.add(Explosion(player.rect.x + 25, player.rect.y + 25, explosion_images))
                game_over = True

            # zásah enemy
            if pygame.sprite.spritecollide(e, bullet_group, True):
                explosion_group.add(Explosion(e.rect.x, e.rect.y, explosion_images))
                e.kill()
                score += 1

        # nová vlna
        if score == new_score:
            new_score += 10
            x, y = 25, -100
            for j in range(2):
                x = 25
                y += 100
                for i in range(5):
                    enemy_group.add(Enemy(x, y))
                    x += 100

        # update
        player_group.update()
        enemy_group.update()
        bullet_group.update()
        enemy_bullet_group.update()
        explosion_group.update()

        # draw
        player_group.draw(screen)
        enemy_group.draw(screen)
        bullet_group.draw(screen)
        enemy_bullet_group.draw(screen)
        explosion_group.draw(screen)

        # score
        score_text = base_font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

        best_text = base_font.render(f"Best: {best}", True, (255, 255, 255))
        screen.blit(best_text, (10, 50))

        # GAME OVER + uložení score
        if game_over and len(explosion_group) == 0:
            if score > best:
                best = score
                with open("score.txt", "w") as s:
                    s.write(str(best))

            state = "MENU"

    pygame.display.flip()
    clock.tick(30)

pygame.quit()