# Write your code below this line 👇
def prime_checker(number):
    if number == 2:
         print(f"{number} is a prime number.")
    elif number > 2:
        x = number // 2 + 1 
        y = x * 2 - 1
        if number == y:
            print(f"{number} is a  prime number. ")
        else:
            print(f"{number} is not a prime number") 
    else:
        print(f"{number} is not a prime number")    




# Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = 87 # Check this number
prime_checker(number=n)


#Chat GPT's answer is below - 
# Write your code above this line 👆


