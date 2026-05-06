import pygame 
import settings
from Python_stickman_jump.pyGame.hry.uhybani_spravna_tvorba.Player import *
from Block import Block
from settings import *

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Uhybani")
running = True
clock = pygame.time.Clock()

score = 0
speed_level = 0

spawn_time = 2000  # začátek: 2 sekundy mezi bloky

base_font = pygame.font.Font(None, 40)

hrac = Player()
hrac_group = pygame.sprite.Group()
hrac_group.add(hrac)

blok_group = pygame.sprite.Group()

with open('score.txt', 'r') as s:
    best = s.read()

SPAWN_BLOK = pygame.USEREVENT + 1
pygame.time.set_timer(SPAWN_BLOK, spawn_time)

while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == SPAWN_BLOK:
            blok_group.add(Block())
            score += 1

    # 🔥 každé 3 body = vyšší obtížnost
    if score // 3 > speed_level:
        speed_level = score // 3

        # 🧱 rychlejší bloky
        settings.BLOCK_SPEED += 1

        # ⏱️ častější spawn (minimálně 400 ms)
        spawn_time = max(400, spawn_time - 150)
        pygame.time.set_timer(SPAWN_BLOK, spawn_time)

    # UPDATE + DRAW
    hrac_group.update()
    hrac_group.draw(screen)

    blok_group.update()
    blok_group.draw(screen)

    # KOLIZE
    if pygame.sprite.spritecollide(hrac, blok_group, True, pygame.sprite.collide_mask):
        print("KOLIZE!")
        pygame.time.delay(1000)

        if int(best) < score:
            with open("score.txt", "w") as soubor:
                soubor.write(str(score))

        running = False

    # TEXTY
    text = "Score: {}".format(score)
    text1 = "Best score: {}".format(best)

    score_text = base_font.render(text, True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    best_score_text = base_font.render(text1, True, (0, 0, 0))
    screen.blit(best_score_text, (300, 10))

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()