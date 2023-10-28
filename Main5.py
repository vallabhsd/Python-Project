import pygame
from Objects import Background

pygame.init()
SCREEN = pygame.display.set_mode((288, 512))

info = pygame.display.Info()
width = info.current_w
height = info.current_h

if width >= height:
    win = SCREEN
else:
    win = SCREEN.convert()
    win = pygame.display.set_mode(win.get_size(), pygame.SCALED | pygame.FULLSCREEN)

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
bg_image = bg_image.convert()
bg_image = pygame.transform.scale(bg_image, win.get_size())

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

    win.blit(bg_image, (bg.x, bg.y))
    pygame.draw.rect(win, ONYX, (0, 0, win.get_width(), win.get_height()), 5, border_radius=4)

    # LIMIT FRAME RATE AND UPDATE DISPLAY

    clock.tick(FPS)
    pygame.display.update()

pygame.quit()

# CLASS Background

class Background(pygame.sprite.Sprite):

    def __init__(self, win):
        super().__init__()

        self.image = bg_image
        self.rect = self.image.get_rect()

        self.x = 0
        self.y = 0

    def update(self, speed):
        self.x += speed

        if self.x >= self.width:
            self.x = 0
