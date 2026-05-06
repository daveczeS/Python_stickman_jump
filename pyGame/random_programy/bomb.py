# import pygame module
import pygame


# import sys library
import sys


# initializing pygame
pygame.init()


clock = pygame.time.Clock()
color = pygame.Color("black")
input_rect = pygame.Rect(200, 200, 140, 32)
# Set the window screen size
display_screen = pygame.display.set_mode((500, 500))

bomb_time = 5
# add font style and size
base_font = pygame.font.Font(None, 40)
# stores text taken by keyboard
text = "Bomba vybuchne za: {}".format(bomb_time)
bomb_timer_text = base_font.render(text, True, (255, 255, 255))
bomb_timer_text_rect = bomb_timer_text.get_rect(center=(250, 250))



running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            bomb_time +=5
   
    
    text = "Bomba vybuchne za: {}".format(bomb_time)

    display_screen.fill((0,0,0))
    
    # render the text
    bomb_timer_text = base_font.render(text, True, (255, 255, 255))
    display_screen.blit(bomb_timer_text, (100, 100))
    bomb_time -=1/60
    if bomb_time < 0:
        running = False
    pygame.display.flip()
    clock.tick(60)
    