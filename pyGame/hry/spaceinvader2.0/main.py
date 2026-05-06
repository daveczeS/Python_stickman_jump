import pygame
import settings
from Player import Player
from Enemy import Enemy
from Bullet import Bullet
from Enemy_Bullet import Enemy_Bullet
from Explosion import Explosion
import random as rand



pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
pygame.display.set_caption("Space Invaders OOP V2")
player = Player()
player_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()
enemy_bullet_group = pygame.sprite.Group()
player_group.add(player)
enemy_bullet = Enemy_Bullet(100,0)
enemy_bullet_group.add(enemy_bullet)
explosion_group = pygame.sprite.Group()
score=0
base_font = pygame.font.Font(None, 40)

explosion_images = []

for i in range(1,6):
    explosion_images.append(pygame.image.load(f"img/exp{i}.png"))

with open('score.txt', 'r') as s:
    best = s.read()

x = 25
y = -100

for j in range(2):
    x =25
    y +=100
    for i in range(5):
        enemy = Enemy(x,y)
        enemy_group.add(enemy)
        x += 100
new_score = 10
strelba = 0

game_over = False

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if strelba <= 0 :
            if event.type == pygame.MOUSEBUTTONDOWN:
                bullet = Bullet(player.rect.x+25,player.rect.y)
                bullet_group.add(bullet)
                strelba = 40
    strelba -=1
    a = 0
    for e in enemy_group:
        a = rand.randint(1,100)
        if a == 25:
            enemy_bullet = Enemy_Bullet(e.rect.x+25,e.rect.y+25)
            enemy_bullet_group.add(enemy_bullet)
        if pygame.sprite.spritecollide(player, enemy_bullet_group, True, pygame.sprite.collide_mask):
            if int(best) < score:
                with open("score.txt", "w") as soubor:
                    soubor.write(str(score))
            player.kill()
            new_explosion = Explosion(player.rect.x+25, player.rect.y+25, explosion_images)
            explosion_group.add(new_explosion)
            game_over = True

        if pygame.sprite.spritecollide(e, player_group, True, pygame.sprite.collide_mask):
            if int(best) < score:
                with open("score.txt", "w") as soubor:
                    soubor.write(str(score))
            player.kill()
            new_explosion = Explosion(player.rect.x+25, player.rect.y+25, explosion_images)
            explosion_group.add(new_explosion)
            game_over = True
        if pygame.sprite.spritecollide(e, bullet_group, True, pygame.sprite.collide_mask):
            new_explosion = Explosion(e.rect.x+25, e.rect.y+25, explosion_images)
            explosion_group.add(new_explosion)
            enemy_group.remove(e)
            score +=1
    if score == new_score:
        x = 25
        y = -100
        new_score += 10       
        for j in range(2):
            x =25
            y +=100
            for i in range(5):
                enemy = Enemy(x,y)
                enemy_group.add(enemy)
                x += 100

    if game_over == True and len(explosion_group) == 0:
        running = False

    screen.fill(settings.BG_COLOR)

    player_group.update()
    player_group.draw(screen)
    enemy_group.update()
    enemy_group.draw(screen)
    bullet_group.update()
    bullet_group.draw(screen)
    enemy_bullet_group.update()
    enemy_bullet_group.draw(screen)
    explosion_group.update()
    explosion_group.draw(screen)
    text = "Score: {}".format(score)
    text1 = "Best score: {}".format(best)

    score_text = base_font.render(text, True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    best_score_text = base_font.render(text1, True, (255, 255, 255))
    screen.blit(best_score_text, (10, 50))
    pygame.display.flip()
    clock.tick(30)
pygame.quit()