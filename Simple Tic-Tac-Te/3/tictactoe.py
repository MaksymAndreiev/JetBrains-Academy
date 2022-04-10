marks = list(input("Enter cells: "))


# check that input has nine items
def check_nine(l):
    if len(l) != 9:
        print("Your input must contain nine items.")


# check that input only contain X, O and _
def check_valid(l):
    for item in l:
        if item.upper() == 'O':
            continue
        elif item.upper() == 'X':
            continue
        elif item == '_':
            continue
        else:
            print("You've entered an invalid item.")


def draw_grid(l):
    top_bottom = "---------"
    print(top_bottom)
    print("| " + l[0] + " " + l[1] + " " + l[2] + " |")
    print("| " + l[3] + " " + l[4] + " " + l[5] + " |")
    print("| " + l[6] + " " + l[7] + " " + l[8] + " |")
    print(top_bottom)


def outcomes(l):
    empty = 0
    x = 0
    o = 0

    for i in range(9):
        if l[i] == "_":
            empty += 1
        elif l[i] == "X":
            x += 1
        else:
            o += 1

    if ((x - o) >= 2) or ((o - x) >= 2):
        print("Impossible")
    else:
        if ((l[0] == l[3] == l[6] == "X")
            or (l[1] == l[4] == l[7] == "X")
            or (l[2] == l[5] == l[8] == "X")
            or (l[0] == l[1] == l[2] == "X")
            or (l[3] == l[4] == l[5] == "X")
            or (l[6] == l[7] == l[8] == "X")
            or (l[0] == l[4] == l[8] == "X")
            or (l[2] == l[4] == l[6] == "X")) and ((l[0] == l[3] == l[6] == "O")
                                                   or (l[1] == l[4] == l[7] == "O")
                                                   or (l[2] == l[5] == l[8] == "O")
                                                   or (l[0] == l[1] == l[2] == "O")
                                                   or (l[3] == l[4] == l[5] == "O")
                                                   or (l[6] == l[7] == l[8] == "O")
                                                   or (l[0] == l[4] == l[8] == "O")
                                                   or (l[2] == l[4] == l[6] == "O")):
            print('Impossible')

        elif ((l[0] == l[3] == l[6] == "X")
              or (l[1] == l[4] == l[7] == "X")
              or (l[2] == l[5] == l[8] == "X")
              or (l[0] == l[1] == l[2] == "X")
              or (l[3] == l[4] == l[5] == "X")
              or (l[6] == l[7] == l[8] == "X")
              or (l[0] == l[4] == l[8] == "X")
              or (l[2] == l[4] == l[6] == "X")):
            print('X wins')

        elif ((l[0] == l[3] == l[6] == "O")
              or (l[1] == l[4] == l[7] == "O")
              or (l[2] == l[5] == l[8] == "O")
              or (l[0] == l[1] == l[2] == "O")
              or (l[3] == l[4] == l[5] == "O")
              or (l[6] == l[7] == l[8] == "O")
              or (l[0] == l[4] == l[8] == "O")
              or (l[2] == l[4] == l[6] == "O")):
            print('O wins')

        elif empty > 0:
            print('Game not finished')

        else:
            print('Draw')


### FUNCTION CALLS ###
# check_nine(marks)
# check_valid(marks)

draw_grid(marks)
outcomes(marks)
