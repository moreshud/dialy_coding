'''
author: moshood olawale
credit: keith galli
project: connect 4 game AI [minmax algorithms]
'''

import numpy as np
import pygame
import sys
import math


#global varaiables
ROW_COUNT = 6
COLUMN_COUNT = 7

BLUE = (0,0,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)



def create_board():
    board = np.zeros((6,7))
    return board

def drop_piece(board, row, col, piece):
    board[row][col] = piece

def is_valid_location(board, col):
    return board[ROW_COUNT - 1][col] == 0 #ternary operator
    
def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r

def print_board(board):
    print(np.flip(board, 0))

def winning_move(board, piece):
    #modified the winning strategy with the former one
    #horizontal location check - video 2
    for col in range(COLUMN_COUNT - 3):
        for row in range(ROW_COUNT):
            if (board[row][col], board[row][col + 1], board[row][col + 2],board[row][col + 3]) == (piece, piece, piece, piece):
                return True

    #row location check
    for col in range(COLUMN_COUNT):
        for row in range(ROW_COUNT - 3):
            if (board[row][col], board[row + 1][col], board[row + 2][col],board[row + 3][col]) == (piece, piece, piece, piece):
                return True

def draw_board(board): 
    for col in range(COLUMN_COUNT):
        for row in range(ROW_COUNT):
            pygame.draw.rect(screen, BLUE, (col*SQUARESIZE, (row+1)*SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(screen, BLACK, (int((col+.5)*SQUARESIZE), int((row + 1.5)*SQUARESIZE)), RADIUS)
            
    for col in range(COLUMN_COUNT):
        for row in range(ROW_COUNT):
            if board[row][col] == 1:
                pygame.draw.circle(screen, RED, (int((col+.5)*SQUARESIZE), height - int((row + .5)*SQUARESIZE)), RADIUS)
            elif board[row][col] == 2:
                pygame.draw.circle(screen, YELLOW, (int((col+.5)*SQUARESIZE), height - int((row + .5)*SQUARESIZE)), RADIUS)
    pygame.display.update()


game_over  = False
board = create_board()  
print_board(board) 
turn = 0

#intialize pygame
pygame.init()

SQUARESIZE = 100
width =  COLUMN_COUNT * SQUARESIZE
height = (ROW_COUNT + 1) * SQUARESIZE
size = (width, height)
RADIUS = int(SQUARESIZE/2 - 5)

screen = pygame.display.set_mode(size)
draw_board(board)
pygame.display.update()

my_font = pygame.font.SysFont("monospace", 75) 



while not game_over:  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, BLACK, (0,0, width, SQUARESIZE))
            posx = event.pos[0]
            if turn == 0:
                pygame.draw.circle(screen, RED, (posx, int(SQUARESIZE/2)), RADIUS)
            else:
                pygame.draw.circle(screen, YELLOW, (posx, int(SQUARESIZE/2)), RADIUS)

        pygame.display.update()
        if event.type == pygame.MOUSEBUTTONDOWN: 
            pygame.draw.rect(screen, BLACK, (0,0, width, SQUARESIZE))
            print(event.pos)           
            #players' input
            if turn == 0:
                posx = event.pos[0]
                col = int(math.floor(posx/SQUARESIZE))
                #modify the validation, "x" does not work because of the board type
                # col = int(input("Player A: Make your selection (0-6): "))

                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 1)

                    if winning_move(board, 1):
                        # print("Player A Wins!!!")
                        label = my_font.render("Player A wins!!!", 1, RED)
                        screen.blit(label, (40,10))
                        game_over = True

            else:
                posx = event.pos[0]
                col = int(math.floor(posx/SQUARESIZE))
                # col = int(input("Player B: Make your selection (0-6): "))

                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 2)
                    
                    if winning_move(board, 2):
                        # print("Player B Wins!!!")
                        label = my_font.render("Player B wins!!!", 1, YELLOW)
                        screen.blit(label, (40,10))
                        game_over = True
            
            print_board(board)
            draw_board(board)

            #alternator/switch 0 - 1
            turn += 1
            turn = turn % 2

            if game_over:
                pygame.time.wait(3000)

