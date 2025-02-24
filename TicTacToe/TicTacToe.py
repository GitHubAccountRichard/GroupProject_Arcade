def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("--" * 5)



def check_winner(board, player):
    win_conditions = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]],
    ]
    return [player, player, player] in win_conditions



def check_full(board):
    for row in board:
        if " " in row:
            return False
    return True



def minimax(board, depth, is_maximizing):
    if check_winner(board, "O"):
        return 1
    elif check_winner(board, "X"):
        return -1
    elif check_full(board):
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    score = minimax(board, depth + 1, False)
                    board[i][j] = " "
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    score = minimax(board, depth + 1, True)
                    board[i][j] = " "
                    best_score = min(score, best_score)
        return best_score



def best_move(board):
    best_score = -float('inf')
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                score = minimax(board, 0, False)
                board[i][j] = " "
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move



def play_game2():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:

        while True:
            try:
                row = int(input("Enter row (1, 2, or 3): ")) - 1
                col = int(input("Enter column (1, 2, or 3): ")) - 1
                if board[row][col] == " ":
                    board[row][col] = "X"
                    break
                else:
                    print("Cell already taken. Try again.")
            except (ValueError, IndexError):
                print("Invalid input. Please enter numbers between 1 and 3.")

        print_board(board)


        if check_winner(board, "X"):
            print("Congratulations! You win!")
            break
        if check_full(board):
            print("It's a tie!")
            break


        move = best_move(board)
        if move:
            board[move[0]][move[1]] = "O"
            print("AI has made its move:")
            print_board(board)


        if check_winner(board, "O"):
            print("Sorry, you lost to the AI.")
            break
        if check_full(board):
            print("It's a tie!")
            break



if __name__ == "__main__":
    play_game2()


