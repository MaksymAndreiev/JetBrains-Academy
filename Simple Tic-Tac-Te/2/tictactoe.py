marks = str(input("Enter cells: "))

# marks = list("O_OXXO_XX")
# marks = list("OXO__X_OX")
# marks = list("_XO__X___")
# marks = list("O_OXbO_XX")
# marks = list("oooxxxooo")
# marks = list("O_OXXO_")

top_bottom = "---------"
l_bound = "| "
r_bound = " |"


# check that marks has nine items
def check_nine(l):
    if len(l) != 9:
        print("Your input must contain nine items.")


# check that marks only contain X, O and _
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
    print(top_bottom)
    print(l_bound + l[0] + " " + l[1] + " " + l[2] + r_bound)
    print(l_bound + l[3] + " " + l[4] + " " + l[5] + r_bound)
    print(l_bound + l[6] + " " + l[7] + " " + l[8] + r_bound)
    print(top_bottom)


### FUNCTION CALLS ###
# check_nine(marks)
# check_valid(marks)
draw_grid(marks)
