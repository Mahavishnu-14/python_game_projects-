import random

def create_board(size, bombs):
    board = [[0 for _ in range(size)] for _ in range(size)]
    bomb_positions = random.sample(range(size * size), bombs)
    for pos in bomb_positions:
        row, col = divmod(pos, size)
        board[row][col] = 'B'
        for i in range(max(0, row - 1), min(size, row + 2)):
            for j in range(max(0, col - 1), min(size, col + 2)):
                if board[i][j] != 'B':
                    board[i][j] += 1
    return board

def print_board(board, revealed):
    size = len(board)
    for i in range(size):
        for j in range(size):
            if revealed[i][j]:
                print(board[i][j], end=' ')
            else:
                print('.', end=' ')
        print()

def reveal(board, revealed, row, col):
    if revealed[row][col]:
        return
    revealed[row][col] = True
    if board[row][col] == 0:
        for i in range(max(0, row - 1), min(len(board), row + 2)):
            for j in range(max(0, col - 1), min(len(board), col + 2)):
                if not revealed[i][j]:
                    reveal(board, revealed, i, j)

def check_win(board, revealed):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] != 'B' and not revealed[i][j]:
                return False
    return True

def play_minesweeper(size=8, bombs=10):
    board = create_board(size, bombs)
    revealed = [[False for _ in range(size)] for _ in range(size)]
    while True:
        print_board(board, revealed)
        row, col = map(int, input("Enter row and column to reveal (e.g., '3 4'): ").split())
        if board[row][col] == 'B':
            print("Game Over! You hit a bomb.")
            break
        reveal(board, revealed, row, col)
        if check_win(board, revealed):
            print("Congratulations! You've cleared the board.")
            break

play_minesweeper()
