'''
author: Moshood Olawale
credit: Christoper T.
project: Tic-Tac-Toe
'''
import os
import random
os.system("clear")

class Board():
    def __init__(self):
        self.cells = ["","","","","","","","","",""]

    def display(self):
        print(" %s | %s | %s" %(self.cells[1], self.cells[2], self.cells[3]))
        print("-----------")
        print(" %s | %s | %s" %(self.cells[4], self.cells[5], self.cells[6]))
        print("-----------")
        print(" %s | %s | %s" %(self.cells[7], self.cells[8], self.cells[9]))
    
    def update_cell(self, cell_no, player):
        if self.cells[cell_no] == "":
            self.cells[cell_no] = player
            #need update for player not to loss turn

    def is_winner(self, player):
        for strategy in [[1,2,3], [4,5,6], [7,8,9],[1,5,9],[3,5,7],[1,4,7],[2,5,8],[3,6,9]]:
            result = True
            for cell_no in strategy:
                if self.cells[cell_no] != player:
                    result = False

            if result == True:
                return True
        return False

        # # if self.cells[1] == player and self.cells[2] == player and self.cells[3] == player:
        # #     return True
        # if self.cells[4] == player and self.cells[5] == player and self.cells[6] == player:
        #     return True
        # if self.cells[7] == player and self.cells[8] == player and self.cells[9] == player:
        #     return True
        # if self.cells[1] == player and self.cells[5] == player and self.cells[9] == player:
        #     return True
        # if self.cells[3] == player and self.cells[5] == player and self.cells[7] == player:
        #     return True
        # if self.cells[1] == player and self.cells[4] == player and self.cells[7] == player:
        #     return True
        # if self.cells[2] == player and self.cells[5] == player and self.cells[8] == player:
        #     return True    
        # if self.cells[3] == player and self.cells[6] == player and self.cells[9] == player:
        #     return True    
        # return False

    def is_tie(self):
        used_cells = 0
        for cell in self.cells:
            if cell != "":
                used_cells += 1
        if used_cells == 9:
            return True
        else:
            return False

    def reset(self):
        self.cells = ["","","","","","","","","",""]

    def ai_move(self, player):
        #if the center is open, choose that
        if player == "X":
            enemy = "O"

        if player == "O":
            enemy = "X"


        if self.cells[5] == "":
            self.update_cell(5, player)
        else:
            while True:
                cell_no = random.randint(1,9)
                if self.cells[cell_no] == "":
                    self.update_cell(cell_no, player)
                    break
        
        #ai can win
        # for i in range(1, 10):
        #     if self.cells[i] == "":
        #         self.cells[i] = player
        #         if self.is_winner(player):
        #             return i
        #         else:
        #             self.cells[i] == ""

        #ai blocks check for the center and defense the strategy down

        #choose random - with quick the other player is at advantage 9-3-6/7
        # for i in range(1,10):
        #     if self.cells[i] == "":
        #         self.update_cell(i, player)
        #         break
        



board = Board()
board.display()

def print_header():
    print("Welcome to Tic-Tac_Toe\n")

def refresh_screen():
    os.system("clear")
    print_header()
    board.display()

# def is_board_full(board):
#     if " " in board:
#         return True
#     else:
#         return False


while True:
    refresh_screen()
    # is_board_full(board)

    #get X input
    x_choice = int(input("\nX) Please choose 1 - 9. >")) #diff raw_input and input

    #update the board
    board.update_cell(x_choice, "X")

    #refresh screen
    refresh_screen()

    #check for X win
    if board.is_winner("X"):
        print("\nX wins! \n")
        
        play_again = input("Would you like to play again? (Y/N): ").upper()
        
        if play_again == "Y":
            board.reset()
            continue
        else:
            break

    if board.is_tie():
        print("\n Ties! \n")
        
        play_again = input("Would you like to play again? (Y/N): ").upper()
        
        if play_again == "Y":
            board.reset()
            continue
        else:
            break

    #get X input
    # o_choice = int(input("\nO) Please choose 1 - 9. >")) #diff raw_input and input

    board.ai_move("O")
    #update the board
    # board.update_cell(o_choice, "O") ai enabled

    #check for X win
    if board.is_winner("O"):
        print("\nO wins! \n")
        
        play_again = input("Would you like to play again? (Y/N): ").upper()
        
        if play_again == "Y":
            board.reset()
            continue
        else:
            break

    if board.is_tie():
        print("\n Tie! \n")
        
        play_again = input("Would you like to play again? (Y/N): ").upper()
        
        if play_again == "Y":
            board.reset()
            continue
        else:
            break

