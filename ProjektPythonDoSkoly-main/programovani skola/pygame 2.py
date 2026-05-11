import pygame, sys
pygame.init()

WIDTH, HEIGHT = 1400, 850
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Stickman Platformer Shapes")
clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 80)
small_font = pygame.font.SysFont(None, 40)

BLACK=(0,0,0); WHITE=(255,255,255)
GREEN=(50,220,100); RED=(220,50,50)
ORANGE=(255,140,0); CYAN=(0,255,255); YELLOW=(255,220,0)

# BACKGROUND
try:
    bg = pygame.image.load("stickman1.jpg").convert()
    bg = pygame.transform.scale(bg,(WIDTH,HEIGHT))
except:
    bg = pygame.Surface((WIDTH,HEIGHT))
    bg.fill((120,190,255))

# ANIMATION
run_frames=[]
for i in range(1,7):
    try:
        img=pygame.image.load(f"run{i}.png").convert_alpha()
        img=pygame.transform.scale(img,(260,260))
        run_frames.append(img)
    except:
        s=pygame.Surface((260,260),pygame.SRCALPHA)
        pygame.draw.rect(s,(50,120,255),(90,50,80,180))
        run_frames.append(s)

frame=0

# PLAYER
player = pygame.Rect(70, HEIGHT-220, 32, 67)
sprite_offset = (-115,-95)

gravity=0.8
vel_y=0
jump=-17
speed=4.5
on_ground=False
facing=True
lives=5

reset_btn = pygame.Rect(WIDTH//2-120,500,240,80)

def reset_player():
    player.x=70
    player.y=HEIGHT-220

# =========================================================
# LEVELY (SKUTEČNÉ TVARY C / S / U / C)
# =========================================================
levels = [

# ---------------- LEVEL 1 - C ----------------
{
"platforms":[
pygame.Rect(0,790,200,60),
pygame.Rect(250,720,150,25),
pygame.Rect(400,650,150,25),
pygame.Rect(550,580,150,25),
pygame.Rect(700,510,150,25),
pygame.Rect(850,440,150,25),
pygame.Rect(1000,370,150,25),
pygame.Rect(1100,300,150,25),
pygame.Rect(1050,200,150,25),
pygame.Rect(900,130,150,25),
pygame.Rect(700,80,150,25),
],
"spikes":[
pygame.Rect(350,760,120,30),
],
"enemies":[
{"rect":pygame.Rect(800,480,50,40),"speed":1,"min":750,"max":1000},
],
"goal":pygame.Rect(650,20,80,80)
},

# ---------------- LEVEL 2 - S ----------------
{
"platforms":[
pygame.Rect(0,790,200,60),
pygame.Rect(220,700,150,25),
pygame.Rect(450,620,150,25),
pygame.Rect(700,700,150,25),
pygame.Rect(950,620,150,25),
pygame.Rect(1100,540,150,25),
pygame.Rect(900,460,150,25),
pygame.Rect(700,380,150,25),
pygame.Rect(500,300,150,25),
pygame.Rect(300,220,150,25),
],
"spikes":[
pygame.Rect(400,760,120,30),
pygame.Rect(850,760,120,30),
],
"enemies":[
{"rect":pygame.Rect(600,600,50,40),"speed":1,"min":550,"max":800},
{"rect":pygame.Rect(800,350,50,40),"speed":1,"min":750,"max":1000},
],
"goal":pygame.Rect(200,150,80,80)
},

# ---------------- LEVEL 3 - U ----------------
{
"platforms":[
pygame.Rect(0,790,180,60),
pygame.Rect(200,700,140,25),
pygame.Rect(350,620,140,25),
pygame.Rect(500,540,140,25),
pygame.Rect(650,460,140,25),
pygame.Rect(800,380,140,25),
pygame.Rect(950,460,140,25),
pygame.Rect(1100,540,140,25),
pygame.Rect(950,300,140,25),
pygame.Rect(800,200,140,25),
pygame.Rect(650,120,140,25),
pygame.Rect(500,60,140,25),
],
"spikes":[
pygame.Rect(250,760,120,30),
pygame.Rect(900,760,120,30),
],
"enemies":[
{"rect":pygame.Rect(700,500,50,40),"speed":2,"min":650,"max":900},
],
"goal":pygame.Rect(450,10,80,80)
},

# ---------------- LEVEL 4 - C HARD ----------------
{
"platforms":[
pygame.Rect(0,790,200,60),
pygame.Rect(230,720,140,25),
pygame.Rect(380,650,140,25),
pygame.Rect(530,580,140,25),
pygame.Rect(680,510,140,25),
pygame.Rect(830,440,140,25),
pygame.Rect(980,370,140,25),
pygame.Rect(1130,300,140,25),
pygame.Rect(1000,220,140,25),
pygame.Rect(850,140,140,25),
pygame.Rect(700,80,140,25),
],
"spikes":[
pygame.Rect(300,760,120,30),
pygame.Rect(700,760,120,30),
pygame.Rect(1050,760,120,30),
],
"enemies":[
{"rect":pygame.Rect(600,500,50,40),"speed":2,"min":550,"max":900},
{"rect":pygame.Rect(900,200,50,40),"speed":2,"min":850,"max":1100},
],
"goal":pygame.Rect(650,20,80,80)
}

]

level=0
state="game"

# =========================================================
# MAIN LOOP
# =========================================================
while True:
    clock.tick(60)

    for e in pygame.event.get():
        if e.type==pygame.QUIT:
            pygame.quit();sys.exit()

        if e.type==pygame.MOUSEBUTTONDOWN and state in ["game_over","win"]:
            if reset_btn.collidepoint(e.pos):
                level=0
                lives=5
                reset_player()
                state="game"

    if state=="game":

        keys=pygame.key.get_pressed()
        move=False

        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            player.x-=speed; facing=False; move=True

        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            player.x+=speed; facing=True; move=True

        if (keys[pygame.K_SPACE] or keys[pygame.K_w]) and on_ground:
            vel_y=jump

        vel_y+=gravity
        player.y+=vel_y

        L=levels[level]
        on_ground=False

        # platforms
        for p in L["platforms"]:
            if player.colliderect(p) and vel_y>0:
                player.bottom=p.top
                vel_y=0
                on_ground=True

        # enemies
        for en in L["enemies"]:
            en["rect"].x+=en["speed"]
            if en["rect"].x<en["min"] or en["rect"].x>en["max"]:
                en["speed"]*=-1
            if player.colliderect(en["rect"]):
                lives-=1
                reset_player()

        # spikes
        for s in L["spikes"]:
            if player.colliderect(s):
                lives-=1
                reset_player()

        # goal
        if player.colliderect(L["goal"]):
            level+=1
            reset_player()
            if level>=len(levels):
                state="win"

        if player.top>HEIGHT:
            lives-=1
            reset_player()

        if lives<=0:
            state="game_over"

        # animation
        if move:
            frame=(frame+0.18)%6
        else:
            frame=0

        # draw
        screen.blit(bg,(0,0))

        for p in L["platforms"]:
            pygame.draw.rect(screen,GREEN,p)

        for s in L["spikes"]:
            pygame.draw.rect(screen,RED,s)

        for en in L["enemies"]:
            pygame.draw.rect(screen,ORANGE,en["rect"])

        pygame.draw.rect(screen,CYAN,L["goal"])

        img=run_frames[int(frame)]
        if not facing:
            img=pygame.transform.flip(img,True,False)

        screen.blit(img,(player.x+sprite_offset[0],player.y+sprite_offset[1]))

        pygame.draw.rect(screen,(255,0,0),player,2)

        screen.blit(small_font.render(f"LEVEL {level+1} | LIVES {lives}",True,BLACK),(20,20))

    elif state=="game_over":
        screen.fill(BLACK)
        screen.blit(font.render("GAME OVER",True,RED),(WIDTH//2-180,250))
        pygame.draw.rect(screen,RED,reset_btn,3)
        screen.blit(small_font.render("RESTART",True,WHITE),(reset_btn.x+55,reset_btn.y+25))

    elif state=="win":
        screen.fill((20,20,20))
        screen.blit(font.render("YOU WIN!",True,YELLOW),(WIDTH//2-150,250))
        pygame.draw.rect(screen,GREEN,reset_btn,3)
        screen.blit(small_font.render("PLAY AGAIN",True,WHITE),(reset_btn.x+30,reset_btn.y+25))

    pygame.display.flip()

pygame.quit()
sys.exit()
