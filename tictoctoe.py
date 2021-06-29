# This Function Draws Game Board
def DrawBoard():
    print(" %c | %c | %c " % (board[0][0], board[0][1], board[0][2]))
    print(" __|___|___")
    print(" %c | %c | %c " % (board[1][0], board[1][1], board[1][2]))
    print(" __|___|___")
    print(" %c | %c | %c " % (board[2][0], board[2][1], board[2][2]))


# PlayerTurn
def PlayerTurn(mark, player, uName):
    while (player % 2 != 0):
        while True:
            num = eval(input(uName + " select a number from 1 to 9: "))
            if num == 1 or num ==2 or num ==3 or num ==4 or num ==5 or num ==6 or num ==7 or num ==8 or num ==9:
                break
            else:
                print("Invalid input,Try Again")
        if num == 1:
            if board[0][0] == ' ':
                board[0][0] = mark
            else:
                print("Following space is not empty,Try again")
                continue
        if num == 2:
            if board[0][1] == ' ':
                board[0][1] = mark
            else:
                print("Following space is not empty,Try again")
                continue
        if num == 3:
            if board[0][2] == ' ':
                board[0][2] = mark
            else:
                print("Following space is not empty,Try again")
                continue
        if num == 4:
            if board[1][0] == ' ':
                board[1][0] = mark
            else:
                print("Following space is not empty,Try again")
                continue
        if num == 5:
            if board[1][1] == ' ':
                board[1][1] = mark
            else:
                print("Following space is not empty,Try again")
                continue
        if num == 6:
            if board[1][2] == ' ':
                board[1][2] = mark
            else:
                print("Following space is not empty,Try again")
                continue
        if num == 7:
            if board[2][0] == ' ':
                board[2][0] = mark
            else:
                print("Following space is not empty,Try again")
                continue
        if num == 8:
            if board[2][1] == ' ':
                board[2][1] = mark
            else:
                print("Following space is not empty,Try again")
                continue
        if num == 9:
            if board[2][2] == ' ':
                board[2][2] = mark
            else:
                print("Following space is not empty,Try again")
                continue
        return num


def blocker(player, turncheck):
    print(turncheck)
    print(player)
    if guess == toss:
        if (player - 1) == 1:
            if (board[1][1] == 'X' or board[1][1] == 'x' or board[1][1] == 'O' or board[1][1] == 'o'):
                if board[0][0] == ' ':
                    board[0][0] = c_mark
                    return
            elif (((board[0][0]) == 'X' or (board[0][0]) == 'x' or ((board[0][1]) == 'x') or (
                    (board[0][1]) == 'X')) or ((board[0][2]) == 'x') or ((board[0][2]) == 'X')) or (
                    (board[1][0]) == 'x') or ((board[1][0]) == 'X') or ((board[1][2]) == 'x') or (
                    (board[1][2]) == 'X') or ((board[2][0]) == 'x') or ((board[2][0]) == 'X') or (
                    (board[2][1]) == 'x') or ((board[2][1]) == 'X') or ((board[2][2]) == 'x') or (
                    (board[2][2]) == 'X') or (((board[0][1]) == ' ' and (board[0][2]) == ' ') and (
                    (board[1][0]) == ' ' and board[2][0] == ' ') and (board[2][2] == ' ')) or (
                    (board[0][0]) == ' ' and (board[0][2]) == ' ') and (
                    (board[1][1]) == ' ' and board[2][1] == ' ') or (
                    (board[0][0]) == ' ' and (board[0][1]) == ' ') and ((board[1][2]) == ' ' and board[2][2] == ' ') and \
                    board[0][2] == ' ' or ((board[0][0]) == ' ' and (board[2][0]) == ' ') and (
                    (board[1][1]) == ' ' and board[1][2] == ' ') or (
                    (board[0][2]) == ' ' and (board[2][2]) == ' ') and (
                    (board[1][1]) == ' ' and board[1][0] == ' ') or (
                    (board[0][0]) == ' ' and (board[1][0]) == ' ') and (
                    (board[0][1]) == ' ' and board[2][1] == ' ') and (board[2][2] == ' ') or (
                    (board[1][1]) == ' ' and (board[0][1]) == ' ') and (
                    (board[2][0]) == ' ' and board[2][2] == ' ') or (
                    (board[0][0]) == ' ' and (board[1][2]) == ' ') and (
                    (board[0][2]) == ' ' and board[2][0] == ' ') and (board[2][1] == ' '):
                if board[1][1] == ' ':
                    board[1][1] = c_mark
                    return
            elif (((board[0][0]) == 'O' or (board[0][0]) == 'o' or ((board[0][1]) == 'o') or (
                    (board[0][1]) == 'O')) or ((board[0][2]) == 'o') or ((board[0][2]) == 'O')) or (
                    (board[1][0]) == 'o') or ((board[1][0]) == 'O') or ((board[1][2]) == 'o') or (
                    (board[1][2]) == 'O') or ((board[2][0]) == 'o') or ((board[2][0]) == 'O') or (
                    (board[2][1]) == 'o') or ((board[2][1]) == 'O') or ((board[2][2]) == 'o') or (
                    (board[2][2]) == 'O') or (((board[0][1]) == ' ' and (board[0][2]) == ' ') and (
                    (board[1][0]) == ' ' and board[2][0] == ' ') and (board[2][2] == ' ')) or (
                    (board[0][0]) == ' ' and (board[0][2]) == ' ') and (
                    (board[1][1]) == ' ' and board[2][1] == ' ') or (
                    (board[0][0]) == ' ' and (board[0][1]) == ' ') and ((board[1][2]) == ' ' and board[2][2] == ' ') and \
                    board[0][2] == ' ' or ((board[0][0]) == ' ' and (board[2][0]) == ' ') and (
                    (board[1][1]) == ' ' and board[1][2] == ' ') or (
                    (board[0][2]) == ' ' and (board[2][2]) == ' ') and (
                    (board[1][1]) == ' ' and board[1][0] == ' ') or (
                    (board[0][0]) == ' ' and (board[1][0]) == ' ') and (
                    (board[0][1]) == ' ' and board[2][1] == ' ') and (board[2][2] == ' ') or (
                    (board[1][1]) == ' ' and (board[0][1]) == ' ') and (
                    (board[2][0]) == ' ' and board[2][2] == ' ') or (
                    (board[0][0]) == ' ' and (board[1][2]) == ' ') and (
                    (board[0][2]) == ' ' and board[2][0] == ' ') and (board[2][1] == ' '):
                if board[1][1] == ' ':
                    board[1][1] = c_mark
                    return
    elif guess != toss:
        if player == 0:
            if board[1][1] == 'X' or board[1][1] == 'x' or board[1][1] == 'O' or board[1][1] == 'o':
                if board[0][0] == ' ':
                    board[0][0] = c_mark
                    return
            elif (((board[0][0]) == 'X' or (board[0][0]) == 'x' or ((board[0][1]) == 'x') or (
                    (board[0][1]) == 'X')) or ((board[0][2]) == 'x') or ((board[0][2]) == 'X')) or (
                    (board[1][0]) == 'x') or ((board[1][0]) == 'X') or ((board[1][2]) == 'x') or (
                    (board[1][2]) == 'X') or ((board[2][0]) == 'x') or ((board[2][0]) == 'X') or (
                    (board[2][1]) == 'x') or ((board[2][1]) == 'X') or ((board[2][2]) == 'x') or (
                    (board[2][2]) == 'X') or (((board[0][1]) == ' ' and (board[0][2]) == ' ') and (
                    (board[1][0]) == ' ' and board[2][0] == ' ') and (board[2][2] == ' ')) or (
                    (board[0][0]) == ' ' and (board[0][2]) == ' ') and (
                    (board[1][1]) == ' ' and board[2][1] == ' ') or (
                    (board[0][0]) == ' ' and (board[0][1]) == ' ') and ((board[1][2]) == ' ' and board[2][2] == ' ') and \
                    board[0][2] == ' ' or ((board[0][0]) == ' ' and (board[2][0]) == ' ') and (
                    (board[1][1]) == ' ' and board[1][2] == ' ') or (
                    (board[0][2]) == ' ' and (board[2][2]) == ' ') and (
                    (board[1][1]) == ' ' and board[1][0] == ' ') or (
                    (board[0][0]) == ' ' and (board[1][0]) == ' ') and (
                    (board[0][1]) == ' ' and board[2][1] == ' ') and (board[2][2] == ' ') or (
                    (board[1][1]) == ' ' and (board[0][1]) == ' ') and (
                    (board[2][0]) == ' ' and board[2][2] == ' ') or (
                    (board[0][0]) == ' ' and (board[1][2]) == ' ') and (
                    (board[0][2]) == ' ' and board[2][0] == ' ') and (board[2][1] == ' '):
                if board[1][1] == ' ':
                    board[1][1] = c_mark
                    return
            elif (((board[0][0]) == 'O' or (board[0][0]) == 'o' or ((board[0][1]) == 'o') or (
                    (board[0][1]) == 'O')) or ((board[0][2]) == 'o') or ((board[0][2]) == 'O')) or (
                    (board[1][0]) == 'o') or ((board[1][0]) == 'O') or ((board[1][2]) == 'o') or (
                    (board[1][2]) == 'O') or ((board[2][0]) == 'o') or ((board[2][0]) == 'O') or (
                    (board[2][1]) == 'o') or ((board[2][1]) == 'O') or ((board[2][2]) == 'o') or (
                    (board[2][2]) == 'O') or (((board[0][1]) == ' ' and (board[0][2]) == ' ') and (
                    (board[1][0]) == ' ' and board[2][0] == ' ') and (board[2][2] == ' ')) or (
                    (board[0][0]) == ' ' and (board[0][2]) == ' ') and (
                    (board[1][1]) == ' ' and board[2][1] == ' ') or (
                    (board[0][0]) == ' ' and (board[0][1]) == ' ') and ((board[1][2]) == ' ' and board[2][2] == ' ') and \
                    board[0][2] == ' ' or ((board[0][0]) == ' ' and (board[2][0]) == ' ') and (
                    (board[1][1]) == ' ' and board[1][2] == ' ') or (
                    (board[0][2]) == ' ' and (board[2][2]) == ' ') and (
                    (board[1][1]) == ' ' and board[1][0] == ' ') or (
                    (board[0][0]) == ' ' and (board[1][0]) == ' ') and (
                    (board[0][1]) == ' ' and board[2][1] == ' ') and (board[2][2] == ' ') or (
                    (board[1][1]) == ' ' and (board[0][1]) == ' ') and (
                    (board[2][0]) == ' ' and board[2][2] == ' ') or (
                    (board[0][0]) == ' ' and (board[1][2]) == ' ') and (
                    (board[0][2]) == ' ' and board[2][0] == ' ') and (board[2][1] == ' '):
                if board[1][1] == ' ':
                    board[1][1] = c_mark
                    return

        # if player choose mid first and then 7
        # vertical check
    if turncheck == 7:
        if (board[1][0] != ' ' and board[1][0] != c_mark) or (board[0][0] != ' ' and board[0][0] != c_mark):
            if ((board[1][0] != ' ') and (board[1][0] != c_mark)) and (board[0][0] == ' '):
                board[0][0] = c_mark
                return
            if (board[0][0] != ' ' and board[0][0] != c_mark) and board[1][0] == ' ':
                board[1][0] = c_mark
                return
                # horizonal check
        if (board[2][1] != ' ' and board[2][1] != c_mark) or (board[2][2] != ' ' and board[2][2] != c_mark):
            if (board[2][1] != ' ' and board[2][1] != c_mark) and board[2][2] == ' ':
                board[2][2] = c_mark
                return
            if (board[2][2] != ' ' and board[2][2] != c_mark) and board[2][1] == ' ':
                board[2][1] = c_mark
                return
                # diagonal check
        if (board[1][1] != ' ' and board[1][1] != c_mark) or (board[0][2] != ' ' and board[0][2] != c_mark):
            if (board[1][1] != ' ' and board[1][1] != c_mark) and board[0][2] == ' ':
                board[0][2] = c_mark
                return
            if (board[0][2] != ' ' and board[0][2] != c_mark) and board[1][1] == ' ':
                board[1][1] = c_mark
                return
                # emptySide check....
                # vertical check
        if (board[1][0] == ' ' and board[0][0] == ' '):
            board[0][0] = c_mark
            return
            # horizontal check
        if (board[2][1] == ' ' and board[2][2] == ' '):
            board[2][2] = c_mark
            return
            # for turncheck 3
    elif turncheck == 3:
        # horizontal Check
        if (board[0][1] != ' ' and board[0][1] != c_mark) or (board[0][0] != ' ' and board[0][0] != c_mark):
            if ((board[0][1] != ' ') and (board[0][1] != c_mark)) and (board[0][0] == ' '):
                board[0][0] = c_mark
                return
            elif (board[0][0] != ' ' and board[0][0] != c_mark) and board[0][1] == ' ':
                board[0][1] = c_mark
                return
                # vertical check
        if (board[1][2] != ' ' and board[1][2] != c_mark) or (board[2][2] != ' ' and board[2][2] != c_mark):
            if (board[1][2] != ' ' and board[1][2] != c_mark) and board[2][2] == ' ':
                board[2][2] = c_mark
                return
            elif (board[2][2] != ' ' and board[2][2] != c_mark) and board[1][2] == ' ':
                board[1][2] = c_mark
                return
                # diagonal check
        if (board[1][1] != ' ' and board[1][1] != c_mark) or (board[2][0] != ' ' and board[2][0] != c_mark):
            if (board[1][1] != ' ' and board[1][1] != c_mark) and board[2][0] == ' ':
                board[2][0] = c_mark
                return
            elif (board[2][0] != ' ' and board[2][0] != c_mark) and board[1][1] == ' ':
                board[1][1] = c_mark
                return
                # emptySide check....
                # vertical check
        if (board[1][2] == ' ' and board[2][2] == ' '):
            board[2][2] = c_mark
            return
            # horizontal check
        if (board[0][1] == ' ' and board[0][0] == ' '):
            board[0][0] = c_mark
            return
            # for TurnCheck 9
    elif turncheck == 9:
        # vertical check
        if (board[1][2] != ' ' and board[1][2] != c_mark) or (board[0][2] != ' ' and board[0][2] != c_mark):
            if ((board[1][2] != ' ') and (board[1][2] != c_mark)) and (board[0][2] == ' '):
                board[0][2] = c_mark
                return
            if (board[0][2] != ' ' and board[0][2] != c_mark) and board[1][2] == ' ':
                board[1][2] = c_mark
                return
                # horizonal check
        if (board[2][1] != ' ' and board[2][1] != c_mark) or (board[2][0] != ' ' and board[2][0] != c_mark):
            if (board[2][1] != ' ' and board[2][1] != c_mark) and board[2][0] == ' ':
                board[2][0] = c_mark
                return
            if (board[2][0] != ' ' and board[2][0] != c_mark) and board[2][1] == ' ':
                board[2][1] = c_mark
                return
                # diagonal check
        if (board[1][1] != ' ' and board[1][1] != c_mark) or (board[0][0] != ' ' and board[0][0] != c_mark):
            if (board[1][1] != ' ' and board[1][1] != c_mark) and board[0][0] == ' ':
                board[0][0] = c_mark
                return
            if (board[0][0] != ' ' and board[0][0] != c_mark) and board[1][1] == ' ':
                board[1][1] = c_mark
                return
        # emptySide check....
        # vertical check
        if (board[1][2] == ' ' and board[0][2] == ' '):
            board[0][2] = c_mark
            return
        # Horizontal check
        if (board[2][1] == ' ' and board[2][0] == ' '):
            board[2][0] = c_mark
            return
    # for TurnCheck 1
    elif turncheck == 1:
        # vertical check
        if (board[1][0] != ' ' and board[1][0] != c_mark) or (board[2][0] != ' ' and board[2][0] != c_mark):
            if ((board[1][0] != ' ') and (board[1][0] != c_mark)) and (board[2][0] == ' '):
                board[2][0] = c_mark
                return
            elif (board[2][0] != ' ' and board[2][0] != c_mark) and board[1][0] == ' ':
                board[1][0] = c_mark
                return
                # horizonal check
        if (board[0][1] != ' ' and board[0][1] != c_mark) or (board[0][2] != ' ' and board[0][2] != c_mark):
            if (board[0][1] != ' ' and board[0][1] != c_mark) and board[0][2] == ' ':
                board[0][2] = c_mark
                return
            elif (board[0][2] != ' ' and board[0][2] != c_mark) and board[0][1] == ' ':
                board[0][1] = c_mark
                return
                # diagonal check
        if (board[1][1] != ' ' and board[1][1] != c_mark) or (board[2][2] != ' ' and board[2][2] != c_mark):
            if (board[1][1] != ' ' and board[1][1] != c_mark) and board[2][2] == ' ':
                board[2][2] = c_mark
                return
            elif (board[2][2] != ' ' and board[2][2] != c_mark) and board[1][1] == ' ':
                board[1][1] = c_mark
                return
        # emptySide check....
        # vertical check
        if (board[1][0] == ' ' and board[2][0] == ' '):
            board[2][0] = c_mark
            return
            # Horizontal check
        if (board[0][1] == ' ' and board[0][2] == ' '):
            board[0][2] = c_mark
            return
            # for TurnCheck 8
    elif turncheck == 8:
        # vertical check
        if (board[1][1] != ' ' and board[1][1] != c_mark) or (board[0][1] != ' ' and board[0][1] != c_mark):
            if ((board[1][1] != ' ') and (board[1][1] != c_mark)) and (board[0][1] == ' '):
                board[0][1] = c_mark
                return
            if (board[0][1] != ' ' and board[0][1] != c_mark) and board[1][1] == ' ':
                board[1][1] = c_mark
                return
                # horizonal check
        if (board[2][0] != ' ' and board[2][0] != c_mark) or (board[2][2] != ' ' and board[2][2] != c_mark):
            if (board[2][0] != ' ' and board[2][0] != c_mark) and board[2][2] == ' ':
                board[2][2] = c_mark
                return
            if (board[2][2] != ' ' and board[2][2] != c_mark) and board[2][0] == ' ':
                board[2][0] = c_mark
                return
        # emptySide check....
        # horizontal check
        if (board[2][0] == ' ' or board[2][2] == ' '):
            if board[2][0] != ' ' and board[2][2] == ' ':
                board[2][2] = c_mark
                return
            if board[2][2] != ' ' and board[2][0] == ' ':
                board[2][0] = c_mark
                return
            if board[2][0] == ' ' and board[2][2] == ' ':
                board[2][0] = c_mark
                return
            # vertical check
        if board[1][1] == ' ' or board[0][1] == ' ':
            if board[1][1] != ' ' and board[0][1] == ' ':
                board[0][1] = c_mark
                return
            if board[0][1] != ' ' and board[1][1] == ' ':
                board[1][1] = c_mark
                return

            # for TurnCheck 2
    elif turncheck == 2:
        # vertical check
        if (board[1][1] != ' ' and board[1][1] != c_mark) or (board[2][1] != ' ' and board[2][1] != c_mark):
            if ((board[1][1] != ' ') and (board[1][1] != c_mark)) and (board[2][1] == ' '):
                board[2][1] = c_mark
                return
            if (board[2][1] != ' ' and board[2][1] != c_mark) and board[1][1] == ' ':
                board[1][1] = c_mark
                return
                # horizonal check
        if (board[0][2] != ' ' and board[0][2] != c_mark) or (board[0][0] != ' ' and board[0][0] != c_mark):
            if (board[0][2] != ' ' and board[0][2] != c_mark) and board[0][0] == ' ':
                board[0][0] = c_mark
                return
            if (board[0][0] != ' ' and board[0][0] != c_mark) and board[0][2] == ' ':
                board[0][2] = c_mark
                return
                # emptySide check....
                # horizontal check
        if (board[0][0] == ' ' or board[0][2] == ' '):
            if board[0][0] != ' ' and board[0][2] == ' ':
                board[0][2] = c_mark
                return
            if board[0][2] != ' ' and board[0][0] == ' ':
                board[0][0] = c_mark
                return
            if board[0][0] == ' ' and board[0][2] == ' ':
                board[0][0] = c_mark
                return
            # vertical check
        if board[1][1] == ' ' or board[2][1] == ' ':
            if board[1][1] != ' ' and board[2][1] == ' ':
                board[2][1] = c_mark
                return
            if board[2][1] != ' ' and board[1][1] == ' ':
                board[1][1] = c_mark
                return
    elif turncheck == 4:
        # vertical check
        if (board[1][1] != ' ' and board[1][1] != c_mark) or (board[1][2] != ' ' and board[1][2] != c_mark):
            if ((board[1][1] != ' ') and (board[1][1] != c_mark)) and (board[1][2] == ' '):
                board[1][2] = c_mark
                return
            if (board[1][2] != ' ' and board[1][2] != c_mark) and board[1][1] == ' ':
                board[1][1] = c_mark
                return
                # horizonal check
        if (board[2][0] != ' ' and board[2][0] != c_mark) or (board[0][0] != ' ' and board[0][0] != c_mark):
            if (board[2][0] != ' ' and board[2][0] != c_mark) and board[0][0] == ' ':
                board[0][0] = c_mark
                return
            if (board[0][0] != ' ' and board[0][0] != c_mark) and board[2][0] == ' ':
                board[2][0] = c_mark
                return
                # emptySide check....
                # vertical
        if (board[0][0] == ' ' or board[2][0] == ' '):
            if board[0][0] != ' ' and board[2][0] == ' ':
                board[2][0] = c_mark
                return
            if board[2][0] != ' ' and board[0][0] == ' ':
                board[0][0] = c_mark
                return
            if board[0][0] == ' ' and board[2][0] == ' ':
                board[0][0] = c_mark
                return

                # Horizontal check
        if board[1][1] == ' ' or board[1][2] == ' ':
            if board[1][1] != ' ' and board[1][2] == ' ':
                board[1][2] = c_mark
                return
            if board[1][2] != ' ' and board[1][1] == ' ':
                board[1][1] = c_mark
                return
            # for TurnCheck 6
    elif turncheck == 6:
        # vertical check
        if (board[1][1] != ' ' and board[1][1] != c_mark) or (board[1][0] != ' ' and board[1][0] != c_mark):
            if ((board[1][1] != ' ') and (board[1][1] != c_mark)) and (board[1][0] == ' '):
                board[1][0] = c_mark
                return
            if (board[1][0] != ' ' and board[1][0] != c_mark) and board[1][1] == ' ':
                board[1][1] = c_mark
                return
                # horizonal check
        if (board[0][2] != ' ' and board[0][2] != c_mark) or (board[2][2] != ' ' and board[2][2] != c_mark):
            if (board[0][2] != ' ' and board[0][2] != c_mark) and board[2][2] == ' ':
                board[2][2] = c_mark
                return
            if (board[2][2] != ' ' and board[2][2] != c_mark) and board[0][2] == ' ':
                board[0][2] = c_mark
                return
                # emptySide check....
                # vertical
        if (board[0][2] == ' ' or board[2][2] == ' '):
            if board[2][2] != ' ' and board[0][2] == ' ':
                board[0][2] = c_mark
                return
            if board[0][2] != ' ' and board[2][2] == ' ':
                board[2][2] = c_mark
                return
            if board[0][2] == ' ' and board[2][2] == ' ':
                board[0][2] = c_mark
                return
            # horizontal check
        if board[1][1] == ' ' or board[1][0] == ' ':
            if (board[1][0] != ' ') and (board[1][1] == ' '):
                board[1][1] = c_mark
                return
            if (board[1][1] != ' ') and (board[1][0] == ' '):
                board[1][0] = c_mark
                return


def checkmate():
    # Horizontal wining move
    if (board[0][0] == board[0][1] and board[0][0] == c_mark and board[0][0] != ' '):
        if board[0][2] == ' ':
            board[0][2] = c_mark
            return True
    if (board[0][1] == board[0][2] and board[0][1] == c_mark and board[0][1] != ' '):
        if board[0][0] == ' ':
            board[0][0] = c_mark
            return True
    if (board[0][0] == board[0][2] and board[0][0] == c_mark and board[0][0] != ' '):
        if board[0][1] == ' ':
            board[0][1] = c_mark
            return True
    if (board[1][0] == board[1][1] and board[1][0] == c_mark and board[1][0] != ' '):
        if board[1][2] == ' ':
            board[1][2] = c_mark
            return True
    if (board[1][1] == board[1][2] and board[1][1] == c_mark and board[1][1] != ' '):
        if board[1][0] == ' ':
            board[1][0] = c_mark
            return True
    if (board[1][0] == board[1][2] and board[1][0] == c_mark and board[1][0] != ' '):
        if board[1][1] == ' ':
            board[1][1] = c_mark
            return True
    if (board[2][0] == board[2][1] and board[2][0] == c_mark and board[2][0] != ' '):
        if board[2][2] == ' ':
            board[2][2] = c_mark
            return True
    if (board[2][1] == board[2][2] and board[2][1] == c_mark and board[2][1] != ' '):
        if board[2][0] == ' ':
            board[2][0] = c_mark
            return True
    if (board[2][0] == board[2][2] and board[2][0] == c_mark and board[2][0] != ' '):
        if board[2][1] == ' ':
            board[2][1] = c_mark
            return True
    # Vertical wining Move
    if (board[0][0] == board[1][0] and board[0][0] == c_mark and board[0][0] != ' '):
        if board[2][0] == ' ':
            board[2][0] = c_mark
            return True
    if (board[1][0] == board[2][0] and board[1][0] == c_mark and board[1][0] != ' '):
        if board[0][0] == ' ':
            board[0][0] = c_mark
            return True
    if (board[0][0] == board[2][0] and board[0][0] == c_mark and board[0][0] != ' '):
        if board[1][0] == ' ':
            board[1][0] = c_mark
            return True
    if (board[0][1] == board[1][1] and board[0][1] == c_mark and board[0][1] != ' '):
        if board[2][1] == ' ':
            board[2][1] = c_mark
            return True
    if (board[1][1] == board[2][1] and board[1][1] == c_mark and board[1][1] != ' '):
        if board[0][1] == ' ':
            board[0][1] = c_mark
            return True
    if (board[0][1] == board[2][1] and board[0][1] == c_mark and board[0][1] != ' '):
        if board[1][1] == ' ':
            board[1][1] = c_mark
            return True
    if (board[0][2] == board[1][2] and board[0][2] == c_mark and board[0][2] != ' '):
        if board[2][2] == ' ':
            board[2][2] = c_mark
            return True
    if (board[1][2] == board[2][2] and board[1][2] == c_mark and board[1][2] != ' '):
        if board[0][2] == ' ':
            board[0][2] = c_mark
            return True
    if (board[0][2] == board[2][2] and board[0][1] == c_mark and board[0][1] != ' '):
        if board[1][2] == ' ':
            board[1][2] = c_mark
            return True
    # diagonal check
    if (board[0][0] == board[1][1] and board[0][0] == c_mark and board[0][0] != ' '):
        if board[2][2] == ' ':
            board[2][2] = c_mark
            return True
    if (board[1][1] == board[2][2] and board[1][1] == c_mark and board[1][1] != ' '):
        if board[0][0] == ' ':
            board[0][0] = c_mark
            return True
    if (board[0][0] == board[2][2] and board[0][0] == c_mark and board[0][0] != ' '):
        if board[1][1] == ' ':
            board[1][1] = c_mark
            return True
    if (board[0][2] == board[1][1] and board[0][2] == c_mark and board[0][2] != ' '):
        if board[2][0] == ' ':
            board[2][0] = c_mark
            return True
    if (board[1][1] == board[2][0] and board[1][1] == c_mark and board[1][1] != ' '):
        if board[0][2] == ' ':
            board[0][2] = c_mark
            return True
    if (board[0][2] == board[2][0] and board[0][2] == c_mark and board[0][2] != ' '):
        if board[1][1] == ' ':
            board[1][1] = c_mark
            return True


# This Function Checks player has won or not
def checkwin():
    global Game
    # wining conditions
    if (board[0][0] == board[0][1] and board[0][1] == board[0][2] and board[0][0] != ' ') or (
            board[1][0] == board[1][1] and board[1][1] == board[1][2] and board[1][0] != ' ') or (
            board[2][0] == board[2][1] and board[2][1] == board[2][2] and board[2][0] != ' ') or (
            board[0][0] == board[1][0] and board[1][0] == board[2][0] and board[0][0] != ' ') or (
            board[0][1] == board[1][1] and board[1][1] == board[2][1] and board[0][1] != ' ') or (
            board[0][2] == board[1][2] and board[1][2] == board[2][2] and board[0][2] != ' ') or (
            board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[1][1] != ' ') or (
            board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[1][1] != ' '):
        Game = Win
        # Match Tie or Draw Condition
    elif (board[0][0] != ' ' and board[0][1] != ' ' and board[0][2] != ' ' and board[1][0] != ' ' and board[1][
        1] != ' ' and board[1][2] != ' ' and board[2][0] != ' ' and board[2][1] != ' ' and board[2][2] != ' '):
        Game = Draw
    else:
        Game = Running

    ##################################################################Main Function#################################################################


play = 'y'

while play == 'Y' or 'y':

    import random

    fb = 'y'
    player = 0
    board = [[' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' ']]
    ########win Flags##########
    Win = 1
    Running = 0
    Game = Running
    Draw = -1
    ###########################    
    print(" ________________________________________________")
    print("")
    print("   W E L C O M E   T O   T I C  T A C  T O E    ")
    print("________________________________________________")

    uName = input("Enter Your Name: ")
    c_mark = " "
    # input check
    while True:
        mark = (input("Select Your Symbol    \'X' or \'O' : ")).upper()
        if mark == 'X' or mark == 'O':
            break
        else:
            print("Invalid Input ,Try Again")

    # comp Mark assignment
    if mark == "X" or mark == "x":
        c_mark = "O"
    elif mark == "O" or mark == "o":
        c_mark = "X"
    # TossChecK
    toss = random.randint(0, 1)
    print(toss)
    guess = eval(input("Enter 0 for Head 1 for Tails: "))
    while not (guess == 1 or guess == 0):
        print("Invalid Input, Try Again")
        guess = eval(input("Enter 0 for Head 1 for Tails: "))
    if guess == toss:
        print(uName + " has Won the Toss,you have 1st turn.")
        player = 1
    else:
        print(toss)
        print(uName + " has lost the toss, Comp has First Turn")
        player = 0
    while Game == Running:
        turncheck = PlayerTurn(mark, player, uName)
        if player % 2 != 0:
            player += 1
        checkwin()
        if (Game == Draw):
            print("Game Draw")
            DrawBoard()
            break
        elif (Game == Win):
            player -= 1
            if (player % 2 != 0):
                print("Computer Won")
                DrawBoard()
                break
            else:
                print(uName + " has Won")
                DrawBoard()
                break

        chk = checkmate()
        if chk:
            print("Computer has Won.")
            DrawBoard()
            break
        blocker(player, turncheck)
        if player % 2 == 0:
            player += 1
        DrawBoard()
        checkwin()
        if (Game == Draw):
            print("Game Draw")
            DrawBoard()
            break
        elif (Game == Win):
            player -= 1
            if (player % 2 != 0):
                print(uName + " has Won")
                DrawBoard()
                break
            else:
                print("Computer Won")
                DrawBoard()
                break
    play = input("Do you Want to Play Again?\n(Y/N)")
    print(uName + " has exited the Game")
    while fb == "y" or fb == 'Y':
        ufb = input("Enter your FeedBack: ")
        fb = input("Do you want to Enter your FeedBack\nPress (Y) for yes\nPress any other Key to exit.")
    print("Thanks for Playing")
    break

###############################################################(FINISHED)#######################################################################
