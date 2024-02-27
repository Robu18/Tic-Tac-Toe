def print_board(board):
    for i in range(0, 9, 3):
        print(" | ".join(board[i:i+3]))
        if i < 6:
            print("-" * 9)


def game_over(board):
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] != " ":
            return True
        if board[3*i] == board[3*i+1] == board[3*i+2] != " ":
            return True
    if board[0] == board[4] == board[8] != " ":
        return True
    if board[2] == board[4] == board[6] != " ":
        return True

    for cell in board:
        if cell == " ":
            return False
    return True


def evaluate(board):
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] == "X":
            return 1
        if board[3*i] == board[3*i+1] == board[3*i+2] == "X":
            return 1
        if board[i] == board[i+3] == board[i+6] == "O":
            return -1
        if board[3*i] == board[3*i+1] == board[3*i+2] == "O":
            return -1
    if board[0] == board[4] == board[8] == "X":
        return 1
    if board[2] == board[4] == board[6] == "X":
        return 1
    if board[0] == board[4] == board[8] == "O":
        return -1
    if board[2] == board[4] == board[6] == "O":
        return -1
    return 0


def minimax(board, depth, alpha, beta, maximizing_player):
    if game_over(board) or depth == 0:
        return evaluate(board)

    if maximizing_player:
        max_eval = float("-inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                eval = minimax(board, depth - 1, alpha, beta, False)
                board[i] = " "
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
        return max_eval
    else:
        min_eval = float("inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                eval = minimax(board, depth - 1, alpha, beta, True)
                board[i] = " "
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
        return min_eval


def best_move(board):
    best_eval = float("-inf")
    best_move = None
    for i in range(9):
        if board[i] == " ":
            board[i] = "X"
            eval = minimax(board, 5, float("-inf"), float("inf"), False)
            board[i] = " "
            if eval > best_eval:
                best_eval = eval
                best_move = i
    return best_move


def play_game():
    board = [" " for _ in range(9)]
    print("--- Tic Tac Toe Game ---")
    print_board(board)
    while not game_over(board):
        player_move = int(input("Enter your move (1-9): ")) - 1
        if player_move < 0 or player_move > 8 or board[player_move] != " ":
            print("Invalid move. Try again.")
            continue
        board[player_move] = "O"
        print_board(board)
        if game_over(board):
            break
        print("Board: ")
        computer_move = best_move(board)
        board[computer_move] = "X"
        print_board(board)
    result = evaluate(board)
    if result == 1:
        print("You lost!")
    elif result == -1:
        print("You win!")
    else:
        print("It's a tie!")


play_game()
