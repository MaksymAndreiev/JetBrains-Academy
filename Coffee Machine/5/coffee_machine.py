# current resources
state = {"water": 400, "milk": 540, "beans": 120, "money": 550, "cups": 9}
# recipe espresso
espresso = {"water": 250, "milk": 0, "beans": 16, "money": 4}
# recipe latte
latte = {"water": 350, "milk": 75, "beans": 20, "money": 7}
# recipe cappuccino
capp = {"water": 200, "milk": 100, "beans": 12, "money": 6}


# process queries
def choose():
    user_input = str(input("Write action (buy, fill, take, remaining, exit): "))
    return user_input


def buy():
    coffee = str(input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino: "))
    if coffee == "1":
        buy_espresso()
    elif coffee == "2":
        buy_latte()
    elif coffee == "3":
        buy_capp()
    elif coffee == "back":
        pass


def buy_espresso():
    # Check: with amounts of [w, m, b, c] available, can we make an espresso?
    for k in espresso:
        if state[k] < espresso[k]:
            print(f"Sorry, not enough {k}!")
            break
    else:
        print("I have enough resources, making you a coffee!")
        # update state according to espresso
        state["water"] -= espresso["water"]
        state["milk"] -= espresso["milk"]
        state["beans"] -= espresso["beans"]
        state["money"] += espresso["money"]
        state["cups"] -= 1


def buy_latte():
    for k in latte:
        if state[k] < latte[k]:
            print(f"Sorry, not enough {k}!")
            break
    else:
        print("I have enough resources, making you a coffee!")
        state["water"] -= latte["water"]
        state["milk"] -= latte["milk"]
        state["beans"] -= latte["beans"]
        state["money"] += latte["money"]
        state["cups"] -= 1


def buy_capp():
    for k in capp:
        if state[k] < capp[k]:
            print(f"Sorry, not enough {k}!")
            break
    else:
        print("I have enough resources, making you a coffee!")
        state["water"] -= capp["water"]
        state["milk"] -= capp["milk"]
        state["beans"] -= capp["beans"]
        state["money"] += capp["money"]
        state["cups"] -= 1


def fill():
    state["water"] += int(input("Write how many ml of water do you want to add: "))
    state["milk"] += int(input("Write how many ml of milk do you want to add: "))
    state["beans"] += int(input("Write how many grams of coffee beans do you want to add: "))
    state["cups"] += int(input("Write how many disposable cups of coffee do you want to add: "))


def take():
    print(f"I gave you ${state['money']}")
    state["money"] = 0


def remaining():
    print(f'''
    The coffee machine has:
    {state["water"]} ml of water
    {state["milk"]} ml of milk
    {state["beans"]} g of coffee beans
    {state["cups"]} disposable cups
    ${state["money"]} dollars of money''')


def machine_on():
    user_input = str(input("Write action (buy, fill, take, remaining, exit): "))
    if user_input == "buy":
        buy()
        print()
        machine_on()
    elif user_input == "fill":
        fill()
        print()
        machine_on()
    elif user_input == "take":
        take()
        print()
        machine_on()
    elif user_input == "remaining":
        remaining()
        print()
        machine_on()
    elif user_input == "exit":
        print("Goodbye")


machine_on()
