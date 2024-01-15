# Write your code below this line 👇
def prime_checker(number):
    if number / 1 == number and number / number == 1 and number is not 2:
        if number // 2 + 1 == number - 1:
            print(f"{number} is a  prime number. ")
    elif number == 2:
        print(f"{number} is a  prime number. ")
    else:
        print(f"{number} is not a prime number")    




# Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = 10 # Check this number
prime_checker(number=n)