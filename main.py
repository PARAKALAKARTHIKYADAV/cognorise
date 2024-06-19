import random

# Define the board
board = [' ' for _ in range(9)]

def print_board():
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print('| ' + ' | '.join(row) + ' |')
    print("\n")

def is_winner(board, player):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), 
                      (0, 3, 6), (1, 4, 7), (2, 5, 8), 
                      (0, 4, 8), (2, 4, 6)]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

def is_board_full(board):
    return ' ' not in board

def make_move(board, position, player):
    if board[position] == ' ':
        board[position] = player
        return True
    return False

def minimax(board, depth, is_maximizing):
    if is_winner(board, 'O'):
        return 1
    elif is_winner(board, 'X'):
        return -1
    elif is_board_full(board):
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(board, depth + 1, False)
                board[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(board, depth + 1, True)
                board[i] = ' '
                best_score = min(score, best_score)
        return best_score

def best_move():
    best_score = -float('inf')
    move = 0
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(board, 0, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    make_move(board, move, 'O')

def main():
    print("Welcome to Tic Tac Toe!")
    print_board()

    while True:
        player_move = int(input("Enter your move (1-9): ")) - 1
        if make_move(board, player_move, 'X'):
            print_board()
            if is_winner(board, 'X'):
                print("You win!")
                break
            elif is_board_full(board):
                print("It's a tie!")
                break

            best_move()
            print_board()
            if is_winner(board, 'O'):
                print("You lose!")
                break
            elif is_board_full(board):
                print("It's a tie!")
                break
        else:
            print("Invalid move, try again.")

if __name__ == '__main__':
    main()
