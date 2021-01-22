X = "X"
O = "O"
EMPTY = ' '
TIE = "Нічия"
NUM_SQUARES = 9

def instruct():
    print("""Щоб зробити хід, введіть від 0 до 8.
0 | 1 | 2
---------
3 | 4 | 5
---------
6 | 7 | 8
""")

def askQuestion(question):
    response = None

    while response not in("y", "n"):
        response = input(question).lower()

    return response

def askNumber(question, low, high):
    response = None

    while response not in range(low, high):
        response = int(input(question))

    return response

def question():
    go_first = askQuestion("Хочете ходити першим? (y/n): ")

    if go_first == "y":
        print ("\nВи граєте хрестиками")
        human = X
        computer = O
    else:
        print("\nВи граєте нуликами")
        computer = X
        human = O

    return computer, human

def newBoard():
    board = []

    for square in range(NUM_SQUARES):
        board.append(EMPTY)

    return board

def  displayBoard(board):
    print("-" * 13)
    for i in range(3):
        print("|", board[i * 3], "|", board[1 + i * 3], "|", board[2 + i * 3], "|")
        print("-" * 13)

def legalMoves(board):
    moves = []

    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)

    return moves

def winner(board):
    WAYS_TO_WIN = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))

    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner
        if EMPTY not in board:
            return TIE
            
    return None

def humanMove(board, human):
    legal = legalMoves(board)
    move = None
    while move not in legal:
        move = askNumber("Твій хід. Виберіть одне з полів (0-8): ", 0, NUM_SQUARES)
        if move not in legal:
            print ("\nЦе поле уже зайнято. Виберіть інше.\n")
    print("Добре.....")

    return move

def computerMove(board, computer, human):
    board = board[:]
    BEST_MOVES = [4, 0, 2, 6, 8, 1, 3, 5, 7]
    print("Мій номер", end = " ")
    for move in legalMoves(board):
        board[move] = computer
        if winner(board) == computer:
            print(move)
            return move
        board[move] = EMPTY
    for move in BEST_MOVES:
        if move in legalMoves(board):
            print(move)
            return move

def nextTurn(turn):
    if turn == X:
        return O
    else:
        return X

def congratWinner(theWinner, computer, human):
    if theWinner != TIE:
        print("Три", theWinner, "під ряд!\n")
    else:
        print("Нічия!\n")
    if theWinner == computer:
        print("Переміг комп'ютер!")
    elif theWinner == human:
        print("Ви перемогли!")
    elif theWinner == TIE:
        print("Нічия!")

def main():
    instruct()
    computer, human = question()
    turn = X
    board = newBoard()
    displayBoard(board)

    while not winner(board):
        if turn == human:
            move = humanMove(board, human)
            board[move] = human
        else:
            move = computerMove(board, computer, human)
            board[move] = computer
        displayBoard(board)
        turn = nextTurn(turn)
    theWinner = winner(board)
    congratWinner(theWinner, computer, human)

main()

if __name__ == "__main__":
    main()	
