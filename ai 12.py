import random

def print_board(board):
    print("-------------")
    for row in board:
        print("|", " | ".join(row), "|")
        print("-------------")

def check_winner(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True

    return False

def is_board_full(board):
    for row in board:
        if ' ' in row:
            return False
    return True

def get_computer_move(board):
    # Simple strategy: Randomly choose an empty spot
    empty_spots = [(row, col) for row in range(3) for col in range(3) if board[row][col] == ' ']
    return random.choice(empty_spots)

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    players = ['X', 'O']
    current_player = random.choice(players)  # Randomly choose who starts

    while True:
        print_board(board)

        if current_player == 'X':
            # Human player's turn
            row = int(input("Enter row (1-3): ")) - 1
            col = int(input("Enter column (1-3): ")) - 1
            if board[row][col] == ' ':
                board[row][col] = 'X'
                current_player = 'O'
            else:
                print("That spot is already taken! Try again.")
                continue
        else:
            # Computer's turn
            row, col = get_computer_move(board)
            board[row][col] = 'O'
            current_player = 'X'

        # Check for a winner or draw
        if check_winner(board, 'X'):
            print_board(board)
            print("X wins!")
            break
        elif check_winner(board, 'O'):
            print_board(board)
            print("O wins!")
            break
        elif is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break

if __name__ == "__main__":
    main()
