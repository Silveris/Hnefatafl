import pygame
import random
pygame.init()

gameSize = 7
squareSize = 80
width = squareSize * gameSize
piece_size = 30

grey = (128, 128, 128)
atker_color = random.randrange(0, 255, 1)
defer_color = random.randrange(0, 255, 1)

test_coord = [120, 40]


def createBoardCoords(side, square_Size):
    coord_dist = square_Size
    coord_start = square_Size / 2

    board = []
    for x in range(side):
        row_array = []
        for y in range(side):
            a = coord_start + coord_dist*y
            b = coord_start + coord_dist*x
            row_array.append([a, b])
        board.append(row_array)
    return board


board_coords = createBoardCoords(gameSize, squareSize)


def drawPiece(team_color, coord, surface, piece_size):
    pygame.draw.circle(surface, team_color, coord, piece_size)


def sevenStart(coordsArray, surface):
    attacker_coords = []
    defender_coords = []









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
    drawPiece(atker_color,test_coord,surface,piece_size)
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
