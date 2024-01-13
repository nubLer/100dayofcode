
print("Thank you for choosing Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L: ").upper() # What size pizza do you want? S, M, or L
add_pepperoni = input("Do you want pepperoni? Y or N: ").upper() # Do you want pepperoni? Y or N
extra_cheese = input("Do you want extra cheese? Y or N: ").upper() # Do you want extra cheese? Y or N
if size == "S":
    size = 15
elif size == "M":
    size = 20
elif size == "L":
    size = 25

if add_pepperoni == "Y" and size == "S":
    add_pepperoni = 2
elif add_pepperoni == "Y":
    add_pepperoni = 3
elif add_pepperoni == "N":
    add_pepperoni = 0

if extra_cheese == "N":
    extra_cheese = 0
elif extra_cheese == "Y":
    extra_cheese = 1

order = size + add_pepperoni + extra_cheese
print(type(order))
print(type(size))
print(type(add_pepperoni))
print(type(extra_cheese))

print(f"Your final bill is: ${order}.")