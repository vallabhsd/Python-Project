import pygame
from Objects import Background

pygame.init()
SCREEN = WIDTH, HEIGHT = 288, 512

info = pygame.display.Info()
width = info.current_w
height = info.current_h

if width >= height:
    win = pygame.display.set_mode(SCREEN)
else:
    win = pygame.display.set_mode(SCREEN, pygame.SCALED | pygame.FULLSCREEN)

pygame.display.set_caption("Scrolling Background")
clock = pygame.time.Clock()
FPS = 24

# COLOURS

BLACK = (0, 0, 0)
ONYX = (40, 40, 43)

# OBJECTS

bg = Background(win)

# IMAGES

bg_image = pygame.image.load('ASSETS/bg.jpeg')
bg_image = pygame.transform.scale(bg_image, (WIDTH, HEIGHT))

# GAME LOOP

is_running = True
while is_running:

    # CHECK FOR EVENTS

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                is_running = False

    # UPDATE BACKGROUND

    bg.update(3)

    # DRAW BACKGROUND

   # play_image_in_circular_repeating_loop(bg_image, win, 0, 0)

    # LIMIT FRAME RATE AND UPDATE DISPLAY

    clock.tick(FPS)
    pygame.display.update()
    pygame.display.flip()

pygame.quit()