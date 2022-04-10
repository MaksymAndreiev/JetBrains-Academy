import math as m

water_avail = int(input("How many ml of water does the coffee machine have: "))
milk_avail = int(input("How many ml of milk does the coffee machine have: "))
bean_avail = int(input("How many grams of beans does the coffee machine have: "))
cups = int(input("How many cups of coffee do you need: "))

# For one cup =
# 200ml water
# 50 ml milk
# 15g coffee beans

water_1c = 200
milk_1c = 50
bean_1c = 15

# With amount of water available, how many cups can we make?
cups_allowed_w = water_avail / water_1c

# With amt of milk available, how many cups can we make?
cups_allowed_m = milk_avail / milk_1c

# with amt of beans available, how many cups can we make?
cups_allowed_b = bean_avail / bean_1c

# find the limiting factor
limit = m.floor(min(cups_allowed_w, cups_allowed_m, cups_allowed_b))

if cups <= limit:
    if limit - cups != 0:
        N = limit - cups
        print(f"Yes, I can make that amount of coffee (and even {N} more than that)")
    else:
        print("Yes, I can make that amount of coffee")
else:
    print(f"No, I can only make {limit} cups of coffee")
