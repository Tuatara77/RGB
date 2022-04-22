import pygame
import random
from rgb import RGB, RGBRotate
from rgbfunc import linear_rgb

FULLSCREEN = False
CHANGERATE = 1
MINBRIGHTNESS = 0
MAXBRIGHTNESS = 255
assert 0 <= MINBRIGHTNESS <= MAXBRIGHTNESS <= 255

STARTCOLOURS = [
	(random.randrange(MINBRIGHTNESS,MAXBRIGHTNESS),                 MINBRIGHTNESS,                                 MAXBRIGHTNESS                ),
	(random.randrange(MINBRIGHTNESS,MAXBRIGHTNESS),                 MAXBRIGHTNESS,                                 MINBRIGHTNESS                ),
	(               MINBRIGHTNESS,                  random.randrange(MINBRIGHTNESS,MAXBRIGHTNESS),                 MAXBRIGHTNESS                ),
	(               MAXBRIGHTNESS,                  random.randrange(MINBRIGHTNESS,MAXBRIGHTNESS),                 MINBRIGHTNESS                ),
	(               MINBRIGHTNESS,                                  MAXBRIGHTNESS,                 random.randrange(MINBRIGHTNESS,MAXBRIGHTNESS)),
	(               MAXBRIGHTNESS,                                  MINBRIGHTNESS,                 random.randrange(MINBRIGHTNESS,MAXBRIGHTNESS))
    ]


def main():
    colour = RGB(*random.choice(STARTCOLOURS))
    # colour = RGB(12,13,14)

    # colour = RGBRotate(255,0,0)
    # colour.set_hue_rotation(2)

    pygame.init()
    pygame.mouse.set_visible(False)
    
    if FULLSCREEN: screen = pygame.display.set_mode([pygame.display.Info().current_w, pygame.display.Info().current_h], pygame.FULLSCREEN)
    else: screen = pygame.display.set_mode([500, 500])

    clock = pygame.time.Clock()
    done = False
    while not done:
        clock.tick_busy_loop(120)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: done = True
                
        if type(colour) == RGB: colour.linear_shift()
        elif type(colour) == RGBRotate: colour.rotate()
        # else: colour = linear_rgb(colour, CHANGERATE, MINBRIGHTNESS, MAXBRIGHTNESS)

        # print(colour.convert_hex())
        # print(colour.getcolour())

        screen.fill(colour.getcolour())
        pygame.display.flip()
    pygame.quit()


def a():
    colour = RGB(255,0,0)
    
    colour = RGBRotate(255,0,0)
    colour.set_hue_rotation(2)

    if type(colour) == RGB:
        for _ in range(10_000_000):
            colour.linear_shift()
            # colour.convert_hex()
    else:
        for _ in range(10_000_000):
            colour.rotate()
        
    # colour = linear_rgb(colour, CHANGERATE, MINBRIGHTNESS, MAXBRIGHTNESS)

import cProfile
if __name__ == "__main__":
    main()
    # cProfile.run("a()")