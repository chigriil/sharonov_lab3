import pygame
from pygame.draw import *
from math import atan

pygame.init()

FPS = 30
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

screen.fill((255, 255, 255))


def draw_with_outline(func, *args, **kwargs):
    """
    COSTIL'!!!!!!!
    """
    args = list(args)
    func(*args)
    args[1] = (0, 0, 0)
    func(*args, 1)


def draw_bg(n=20):
    """
    :param n: count of fence elements
    """
    # sky
    rect(screen, (0, 255, 255), (0, 0, SCREEN_WIDTH, SCREEN_HEIGHT // 5))

    # grass
    rect(screen, (0, 255, 100), (0, 3 * SCREEN_HEIGHT // 5, SCREEN_WIDTH, 2 * SCREEN_HEIGHT // 5))

    # fence
    rect(screen, (255, 255, 0), (0, SCREEN_HEIGHT // 5, SCREEN_WIDTH, 2 * SCREEN_HEIGHT // 5))
    line(screen, (0, 0, 0), (0, 3 * SCREEN_HEIGHT // 5), (SCREEN_WIDTH, 3 * SCREEN_HEIGHT // 5))
    for x_coord in range(0, SCREEN_WIDTH, SCREEN_WIDTH // n):
        line(screen, (0, 0, 0), (x_coord, SCREEN_HEIGHT // 5), (x_coord, 3 * SCREEN_HEIGHT // 5))


def draw_chain(x, y):
    # TODO: make it better
    for i in range(10):
        circle(screen, (0, 0, 0), (x - i * SCREEN_WIDTH // 70 + SCREEN_WIDTH // 15, y + i * SCREEN_HEIGHT // 100),
               SCREEN_HEIGHT // 100, 1)


def draw_kennel(x, y):
    def poly_with_outline(points, color):
        polygon(screen, color, points)
        polygon(screen, (0, 0, 0), points, 1)

    front = (
        (x, y),
        (x, y - SCREEN_HEIGHT // 7),
        (x + SCREEN_WIDTH // 6, y - SCREEN_HEIGHT // 7 + SCREEN_HEIGHT // 15),
        (x + SCREEN_WIDTH // 6, y + SCREEN_HEIGHT // 15),
    )

    right = (
        (x + SCREEN_WIDTH // 6, y - SCREEN_HEIGHT // 7 + SCREEN_HEIGHT // 15),
        (x + SCREEN_WIDTH // 6, y + SCREEN_HEIGHT // 15),
        (x + SCREEN_WIDTH // 6 + SCREEN_WIDTH // 6, y + SCREEN_HEIGHT // 15 - SCREEN_HEIGHT // 20),
        (x + SCREEN_WIDTH // 6 + SCREEN_WIDTH // 6, y + SCREEN_HEIGHT // 15 - SCREEN_HEIGHT // 20 - SCREEN_HEIGHT // 7)
    )

    roof_front = (
        (x, y - SCREEN_HEIGHT // 7),
        (x + SCREEN_WIDTH // 6, y - SCREEN_HEIGHT // 7 + SCREEN_HEIGHT // 15),
        (x + SCREEN_WIDTH // 6 - SCREEN_WIDTH // 16, y - SCREEN_HEIGHT // 7 + SCREEN_HEIGHT // 15 - SCREEN_HEIGHT // 6),

    )

    roof_right = (
        (x + SCREEN_WIDTH // 6, y - SCREEN_HEIGHT // 7 + SCREEN_HEIGHT // 15),
        (x + SCREEN_WIDTH // 6 - SCREEN_WIDTH // 16, y - SCREEN_HEIGHT // 7 + SCREEN_HEIGHT // 15 - SCREEN_HEIGHT // 6),
        (x + SCREEN_WIDTH // 6 - SCREEN_WIDTH // 16 + SCREEN_WIDTH // 6,
         y - SCREEN_HEIGHT // 7 + SCREEN_HEIGHT // 15 - SCREEN_HEIGHT // 6 - SCREEN_HEIGHT // 20),
        (x + SCREEN_WIDTH // 6 + SCREEN_WIDTH // 6, y - SCREEN_HEIGHT // 7 + SCREEN_HEIGHT // 15 - SCREEN_HEIGHT // 20),
    )

    poly_with_outline(front, (220, 255, 0))
    poly_with_outline(right, (220, 255, 0))
    poly_with_outline(roof_front, (255, 255, 0))
    poly_with_outline(roof_right, (255, 255, 0))

    # black hole
    circle(screen, (0, 0, 0), (x + SCREEN_WIDTH // 12, y - SCREEN_WIDTH // 30), 35)

    # chain
    draw_chain(x, y)


def draw_dog(x, y, color=(120, 120, 120)):
    def draw_head():
        draw_with_outline(
            rect,
            screen, color, (x, y, SCREEN_WIDTH // 10, SCREEN_HEIGHT // 10))

        draw_with_outline(
            ellipse,
            screen, color, ((x - SCREEN_WIDTH // 40, y), (SCREEN_WIDTH // 30, SCREEN_HEIGHT // 20)))

        draw_with_outline(
            ellipse,
            screen, color,
            ((x + SCREEN_WIDTH // 40 + SCREEN_WIDTH // 15, y), (SCREEN_WIDTH // 30, SCREEN_HEIGHT // 20)))

    def draw_eyes():
        ellipse(screen,
                (255, 255, 255),
                ((x + SCREEN_WIDTH // 80, y + SCREEN_HEIGHT // 30),
                 (SCREEN_WIDTH // 30, SCREEN_HEIGHT // 80)))
        ellipse(screen,
                (255, 255, 255),
                ((x - SCREEN_WIDTH // 80 + SCREEN_WIDTH // 10 - SCREEN_WIDTH // 30, y + SCREEN_HEIGHT // 30),
                 (SCREEN_WIDTH // 30, SCREEN_HEIGHT // 80)))
        circle(screen,
               (0, 0, 0),
               (x + SCREEN_WIDTH // 80 + SCREEN_WIDTH // 60,
                y + SCREEN_HEIGHT // 30 + SCREEN_HEIGHT // 160),
               SCREEN_HEIGHT // 150)
        circle(screen,
               (0, 0, 0),
               (x - SCREEN_WIDTH // 80 + SCREEN_WIDTH // 10 - SCREEN_WIDTH // 60,
                y + SCREEN_HEIGHT // 30 + SCREEN_HEIGHT // 160),
               SCREEN_HEIGHT // 150)

    def draw_body():
        def draw_front_leg(x, y):
            ellipse(screen, color,
                    ((x - SCREEN_WIDTH // 40, y + SCREEN_HEIGHT // 15), (SCREEN_WIDTH // 15, SCREEN_HEIGHT // 7)))
            ellipse(screen, color, ((x - SCREEN_WIDTH // 25, y + SCREEN_HEIGHT // 6 + SCREEN_HEIGHT // 50),
                                    (SCREEN_WIDTH // 15, SCREEN_HEIGHT // 30)))

        ellipse(screen, color, ((x, y + SCREEN_HEIGHT // 30), (SCREEN_WIDTH // 5, SCREEN_HEIGHT // 10)))
        ellipse(screen, color,
                ((x + SCREEN_WIDTH // 10, y - SCREEN_HEIGHT // 50), (SCREEN_WIDTH // 5, SCREEN_HEIGHT // 10)))
        draw_front_leg(x, y)
        draw_front_leg(x + SCREEN_WIDTH // 10, y + SCREEN_HEIGHT // 25)
        draw_front_leg(x + SCREEN_WIDTH // 4, y - SCREEN_HEIGHT // 25)
        draw_front_leg(x + SCREEN_WIDTH // 4 - SCREEN_WIDTH // 10, y - 2 * SCREEN_HEIGHT // 25)

    draw_body()
    draw_head()
    draw_eyes()


draw_bg()
draw_kennel(500, 650)
draw_dog(100, 550)
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
