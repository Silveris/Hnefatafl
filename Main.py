import pygame
import random
pygame.init()

gameSize = 11
squareSize = 80
width = squareSize * gameSize

grey = (128, 128, 128)
atker = random.randrange(0, 255, 1)
defer = random.randrange(0, 255, 1)


def drawGrid(w, rows, surface):
    sizeBtwn = (1/rows)*w

    x = 0
    y = 0
    for l in range(rows):
        x = x + sizeBtwn
        y = y + sizeBtwn

        pygame.draw.line(surface, (0, 0, 0), (x, 0), (x, w))
        pygame.draw.line(surface, (0, 0, 0), (0, y), (w, y))


def redrawWindow(surface):

    surface.fill((143, 188, 143))
    drawGrid(width, gameSize, surface)
    pygame.display.update()


# Creates and names the game window
window = pygame.display.set_mode((width, width))
pygame.display.set_caption("Hnefatafl")


# Main Game loop
run = True
while run:
    pygame.time.delay(60)

    # Lets the 'x' button in the top right corner quit the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    redrawWindow(window)
