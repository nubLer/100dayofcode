#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 
't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

letter_list = []
numbers_list = []
symbols_list = []

nr_letters_stuff = range(1, nr_letters + 1)
nr_letters = list(nr_letters_stuff)
nr_symbols_stuff = range(1, nr_symbols + 1)
nr_symbols = list(nr_symbols_stuff)
nr_number_stuff = range(1, nr_numbers + 1)
nr_numbers = list(nr_number_stuff)

for num in nr_letters:
    letter_list.append(random.choice(letters))
for num in nr_symbols:
    symbols_list.append(random.choice(symbols))
for num in nr_numbers:
    numbers_list.append(random.choice(numbers))

password = letter_list + numbers_list + symbols_list
random.shuffle(password)
password = str(password)
Final_password = password.replace("'","").replace(",","").replace("[", "").replace("]","")
print(f"Your secure password is: {Final_password}")



the_string = ["Hello", "world", "in", "Python"]
the_new_string = str(the_string)
the_new_string = "".join(the_string)
print(the_new_string)