espresso = {"water": 250, "milk": 0, "beans": 16, "money": 4}
latte = {"water": 350, "milk": 75, "beans": 20, "money": 7}
capuccino = {"water": 200, "milk": 100, "beans": 12, "money": 6}
coffee = {"water": 200, "milk": 50, "beans": 15}

print("Write how many cups of coffee you will need:\n")
c = int(input())
print(f"For {c} cups of coffee you will need:\n"
      f"{c * coffee['water']} ml of water\n"
      f"{c * coffee['milk']} ml of milk\n"
      f"{c * coffee['beans']} g of coffee beans")
