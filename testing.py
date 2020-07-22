import pygame
import random
from string import ascii_lowercase

gameSize = 7
squareSize = 80
width = squareSize * gameSize
piece_size = 30


def createBoardCoords(side, squareSize):
    coord_dist = squareSize
    coord_start = squareSize / 2

    board = []
    for x in range(side):
        row_array = []
        for y in range(side):
            a = coord_start + coord_dist*y
            b = coord_start + coord_dist*x
            row_array.append([a, b])
        board.append(row_array)
    return board


board = createBoardCoords(gameSize, squareSize)

lat = []
for line in board:
    lat.append(line[3])
lng = board[3]

atk_coord = []
def_coord = []

print(lat)
print(lng)


# print(f'atk {atk_coord}')
# print(f'def {def_coord}')








