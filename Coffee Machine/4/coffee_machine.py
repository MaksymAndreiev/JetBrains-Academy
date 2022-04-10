state = {"water": 400,
         "milk": 540,
         "beans": 120,
         "cups": 9,
         "money": 550}

# print the coffee machine's state
print(f'''
The coffee machine has:
{state["water"]} ml of water
{state["milk"]} ml of milk
{state["beans"]} g of coffee beans
{state["cups"]} disposable cups
{state["money"]} dollars of money''')

# recipe espresso
espresso = {"water": 250,
            "milk": 0,
            "beans": 16,
            "cups": 1,
            "cost": 4}

# recipe latte
latte = {"water": 350,
         "milk": 75,
         "beans": 20,
         "cups": 1,
         "cost": 7}

# recipe cappuccino
cappuccino = {"water": 200,
              "milk": 100,
              "beans": 12,
              "cups": 1,
              "cost": 6}


# process queries
# first ask if they want to buy, fill or take
def choose():
    user_input = str(input("Write action (buy, fill, take): "))
    return user_input


def buy():
    coffee = int(input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino: "))
    if coffee == 1:
        # update state according to espresso
        state["water"] = state["water"] - espresso["water"]
        state["milk"] = state["milk"] - espresso["milk"]
        state["beans"] = state["beans"] - espresso["beans"]
        state["cups"] = state["cups"] - espresso["cups"]
        state["money"] = state["money"] + espresso["cost"]
    elif coffee == 2:
        print("You chose a latte. Pretty standard.")
        # update state according to latte
        state["water"] = state["water"] - latte["water"]
        state["milk"] = state["milk"] - latte["milk"]
        state["beans"] = state["beans"] - latte["beans"]
        state["cups"] = state["cups"] - latte["cups"]
        state["money"] = state["money"] + latte["cost"]
    elif coffee == 3:
        print("You chose a cappuccino. Foamy!")
        # update state according to cappuccino
        state["water"] = state["water"] - cappuccino["water"]
        state["milk"] = state["milk"] - cappuccino["milk"]
        state["beans"] = state["beans"] - cappuccino["beans"]
        state["cups"] = state["cups"] - cappuccino["cups"]
        state["money"] = state["money"] + cappuccino["cost"]


def fill():
    print("You chose to replenish the supplies. Thank you!")
    add_water = int(input("Write how many ml of water do you want to add: "))
    add_milk = int(input("Write how many ml of milk do you want to add: "))
    add_beans = int(input("Write how many grams of coffee beans do you want to add: "))
    add_cups = int(input("Write how many disposable cups of coffee do you want to add: "))

    state["water"] += add_water
    state["milk"] += add_milk
    state["beans"] += add_beans
    state["cups"] += add_cups


def take():
    print(f"I gave you ${state['money']}")
    state["money"] = 0


user_input = choose()
if user_input == "buy":
    buy()
elif user_input == "fill":
    fill()
elif user_input == "take":
    take()

# print the coffee machine's state after processing
print(f'''
The coffee machine has:
{state["water"]} ml of water
{state["milk"]} ml of milk
{state["beans"]} g of coffee beans
{state["cups"]} disposable cups
{state["money"]} dollars of money''')
