import pygame
pygame.init()

# --- Rozlišení ---
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600

# --- Font ---
menu_font = pygame.font.SysFont("Arial", 50)

# --- Menu texty ---
title_text = menu_font.render("SPACE INVADERS", True, (255, 255, 255))
play_text = menu_font.render("PLAY", True, (255, 255, 255))
settings_text = menu_font.render("SETTINGS", True, (255, 255, 255))
quit_text = menu_font.render("QUIT", True, (255, 255, 255))

# --- Settings texty ---
res800_text = menu_font.render("800x600", True, (255, 255, 255))
res1024_text = menu_font.render("1024x768", True, (255, 255, 255))
res1280_text = menu_font.render("1280x960", True, (255, 255, 255))
back_text = menu_font.render("BACK", True, (255, 255, 255))

# --- Recty (budou dynamické) ---
title_rect = play_rect = settings_rect = quit_rect = None
res800_rect = res1024_rect = res1280_rect = back_rect = None

# --- Funkce pro aktualizaci rectů ---
def update_rects():
    global title_rect, play_rect, settings_rect, quit_rect
    global res800_rect, res1024_rect, res1280_rect, back_rect

    title_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT * 0.1))
    play_rect = play_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT * 0.3))
    settings_rect = settings_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT * 0.5))
    quit_rect = quit_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT * 0.7))

    res800_rect = res800_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT * 0.3))
    res1024_rect = res1024_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT * 0.45))
    res1280_rect = res1280_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT * 0.6))
    back_rect = back_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT * 0.8))

# --- Zavoláme hned při startu ---
update_rects()

# --- Player settings ---
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 50
PLAYER_SPEED = 5
PLAYER_IMAGE_PATH = "obrazky/spaceship.png"  # <- uprav cestu podle tvého souboru

# --- Enemy settings ---
ENEMY_IMAGE_PATH = "img/alien1.png"

BULLET_IMAGE_PATH = "img/bullet.png"