#This funcion will caculate and return the factorial of the users input
def recursive_factorial(new_int):
  if new_int == 1:
    return 1
  else:
    return new_int * recursive_factorial(new_int-1)

# This loop will only alow the user to input an integer
while True:
    try:
       user_int = int(input("What integer would you like to find the factorial of? "))
       break
    except ValueError:
       print("Please Enter An Integer")
       continue
    else:
        break

# Prints the factorial of the User's input
print(recursive_factorial(user_int))