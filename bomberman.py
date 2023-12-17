import os
import random


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def check_if_end(board, number_of_flags, number_of_bombs, size):
    num_checked = 0
    good_spot = 0
    for i in range(size):
        for j in range(size):
            if board[0][i][j] == 1:
                num_checked += 1
            if number_of_flags == 0 and (board[0][i][j] == 2 or board[1][i][j] == '☺'):
                good_spot += 1
    
    if (size**2 == num_checked + number_of_bombs) or good_spot == number_of_bombs:
        return True
    
    

def show_empty(board, size, position_x, position_y):
    queue = []
    queue.append(Point(position_x, position_y))
    while queue != []:
        now = queue.pop(0)
        for i in range(now.x - 1, now.x + 2):
            for j in range(now.y - 1, now.y + 2):
                if 0 <= i < size and 0 <= j < size and board[0][j][i] != 1:
                    if board[1][j][i] == ' ':
                        queue.append(Point(i, j))
                    board[0][j][i] = 1

def show_board(board, size):
    for i in range(size + 2):
        for j in range(size + 2):
            if i in [0, size + 1] or j in [0, size + 1]:
                print('\u2588', end = '')
            elif board[0][i - 1][j - 1] == 0 and board[1][i - 1][j - 1] != '☺':
                print('\u2592', end='')
            elif board[0][i - 1][j - 1] == 1 or board[1][i - 1][j - 1] == '☺':
                print(board[1][i - 1][j - 1], end='')
        print()
                

def draw_board(board, size, number_of_bombs, position_x, position_y):
    bomb_count = 0
    while bomb_count < number_of_bombs:
        random_x = random.randint(0, size - 1)
        random_y = random.randint(0, size - 1)
        if random_x != position_x and random_y != position_y and board[1][random_y][random_x] != '☺':
            board[1][random_y][random_x] = '☺'
            bomb_count += 1
    
    for i in range(size):
        for j in range(size):
            num = 0
            if board[1][i][j] != '☺':
                for l in range(i - 1, i + 2):
                    for o in range(j - 1, j + 2):
                        if 0 <= l < size and 0 <= o < size:
                            if board[1][l][o] == '☺':
                                num += 1
            if num != 0:
                board[1][i][j] = num
     

def print_game(board, size, position_x, position_y):
    for i in range(size + 2):
        for j in range(size + 2):
            if i - 1 == position_y and j - 1 == position_x:
                print('*', end='')
            elif i in [0, size + 1] or j in [0, size + 1]:
                print('\u2588', end = '')
            elif board[0][i - 1][j - 1] == 2:
                print('☻', end = '')
            elif board[0][i - 1][j - 1] == 1:
                print(board[1][i - 1][j - 1], end='')
            else:
                print('\u2592', end='')
        print()

def game(size, number_of_bombs):
    board = [[[0 for i in range(size)] for j in range(size)] for k in range(2)]
    for i in range(size):
        for j in range(size):
            board[1][i][j] = ' '
            
    position_x = 0
    position_y = 0
    move = 0
    number_of_flags = number_of_bombs
    while True:
        os.system('cls')
        print_game(board, size, position_x, position_y)
        input_move = input(f"make move: ")
        if input_move == 'w':
            if position_y != 0:
                position_y -= 1
        elif input_move == 's':
            if position_y != size - 1:
                position_y += 1
        elif input_move == 'a':
            if position_x != 0:
                position_x -= 1
        elif input_move == 'd':
            if position_x != size - 1:
                position_x += 1
        elif input_move == ' ':
            if board[0][position_y][position_x] == 0:
                board[0][position_y][position_x] = 1
                if move == 0:
                    draw_board(board, size, number_of_bombs, position_x, position_y)
                if board[1][position_y][position_x] == ' ':
                    show_empty(board, size, position_x, position_y)
                elif board[1][position_y][position_x] == '☺':
                    os.system('cls')
                    show_board(board, size)
                    print('GAME OVER')
                    input()
                    return
                move += 1
        elif input_move == 'end':
            os.system('cls')
            show_board(board, size)
            input()
            return
        elif input_move == 'o':
            if board[0][position_y][position_x] == 0 and number_of_flags > 0:
              board[0][position_y][position_x] = 2
              number_of_flags -= 1
            elif board[0][position_y][position_x] == 2:
                board[0][position_y][position_x] = 0
                number_of_flags += 1     
        if check_if_end(board, number_of_flags, number_of_bombs, size):
            os.system('cls')
            show_board(board, size)
            print('CONGRATULATIONS!!!! YOU WON!!!')
            input()
            return
            
    

while True:
    os.system('cls')
    size = int(input(f"Select size of the board: "))
    custom_number_of_bombs = input(f"Do you want to set custom number of bombs? yes/no: ")
    if custom_number_of_bombs == 'yes':
        number_of_bombs = int(input(f"Select number of bombs: "))
        while number_of_bombs > size**2:
            print("Incorrect number of bombs!!!")
            number_of_bombs = int(input(f"Select number of bombs: "))
    else :
        number_of_bombs = int(size**2 * 0.15625)

    game(size, number_of_bombs)
    
    
    print(chr(2))