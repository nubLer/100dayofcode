# Write your code below this line 👇
def prime_checker(number):
    if number == 2:
         print("It's a prime number.")
    elif number > 2:
        x = number // 2 + 1 
        y = x * 2 - 1
        if number == y:
            print("It's a prime number.")
        else:
            print("It's not a prime number.") 
    else:
        print("It's not a prime number.")    




# Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = 87 # Check this number
prime_checker(number=n)


#Chat GPT's answer is below - same as instructors : 
# Write your code above this line 👆


# Write your code below this line 👇
def prime_checker(number):
    is_prime = True
    for i in range(2, number):
      if number % i == 0:
          is_prime = False
    if is_prime:  
        print("It's a prime number.")
    else:
        print("It's not a prime number.")
# Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input()) # Check this number
prime_checker(number=n)