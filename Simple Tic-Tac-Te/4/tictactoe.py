from textwrap import wrap

user_input = input("Enter cells: ")
table = [wrap(x, 1) for x in wrap(user_input, 3)]
sep_line = "-" * 9
line = "|"
test = '123456789 '
test2 = '123 '
isTrue = True


# print(table)


def count_cmb(smb):  # counts X or O in table
    return len([i for j in table for i in j if i == smb])


def check_win(smb):
    if table[0][0] == smb and table[1][1] == smb and table[2][2] == smb:
        return True
    elif table[0][2] == smb and table[1][1] == smb and table[2][0] == smb:
        return True
    elif table[0][0] == smb and table[1][0] == smb and table[2][0] == smb:
        return True
    elif table[0][1] == smb and table[1][1] == smb and table[2][1] == smb:
        return True
    elif table[0][2] == smb and table[1][2] == smb and table[2][2] == smb:
        return True
    elif table[0][0] == smb and table[0][1] == smb and table[0][2] == smb:
        return True
    elif table[1][0] == smb and table[1][1] == smb and table[1][2] == smb:
        return True
    elif table[2][0] == smb and table[2][1] == smb and table[2][2] == smb:
        return True
    else:
        return False


def print_row(row_number):
    return " ".join([i for i in table[row_number]])


def check_empty_cells():
    return "_" in [elem for sublist in table for elem in sublist]


def result():
    global isTrue
    if check_win("X") and check_win("O"):
        print("Impossible")
        isTrue = False
    elif count_cmb("X") - count_cmb("O") > 1 or count_cmb("O") - count_cmb("X") > 1:
        print("Impossible")
        isTrue = False
    elif check_win("X"):
        print("X wins")
        isTrue = False
    elif check_win("O"):
        print("O wins")
        isTrue = False
    # elif check_empty_cells() and not check_win("X") and not check_win("O"):  # убрать в след раз
    #     print("Game not finished")
    elif not check_empty_cells():
        print("Draw")
        isTrue = False


def damn_table(damn_coord):
    global x
    global y
    if damn_coord == "1 3":
        x = 2
        y = 0
    elif damn_coord == "1 2":
        x = 1
        y = 0
    elif damn_coord == "1 1":
        x = 0
        y = 0
    elif damn_coord == "2 3":
        x = 2
        y = 1
    elif damn_coord == "2 2":
        x = 1
        y = 1
    elif damn_coord == "2 1":
        x = 0
        y = 1
    elif damn_coord == "3 3":
        x = 2
        y = 2
    elif damn_coord == "3 2":
        x = 1
        y = 2
    elif damn_coord == "3 1":
        x = 0
        y = 2


table_format = f"""
{sep_line}
{line} {print_row(0)} {line}
{line} {print_row(1)} {line}
{line} {print_row(2)} {line}
{sep_line}"""

print(table_format)

while isTrue:
    user_move = input("Enter the coordinates: ")

    if not all(item in test for item in user_move):
        print("You should enter numbers!")
        continue
    elif len(user_move) > 3:
        print("You should enter numbers!")
        continue
    elif not all(item in test2 for item in user_move):
        print("Coordinates should be from 1 to 3!")
        continue
    else:
        # x = 0
        # y = 0
        damn_table(user_move)
        if table[y][x] == "_":
            table[y][x] = "X"
            print(f"""
{sep_line}
{line} {print_row(0)} {line}
{line} {print_row(1)} {line}
{line} {print_row(2)} {line}
{sep_line}""")
            result()
            break  # continue
        else:
            print("This cell is occupied! Choose another one!")
            continue
