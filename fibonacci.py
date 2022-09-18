# This program will calculate and display the nth number in the Fibonacci sequence

# Initial variables/Lists
integer_list = []

# This loop will only alow the user to input an integer
while True:
    try:
       user_input = int(input("What integer would you like to from the Fibonacci sequence? "))
       break
    except ValueError:
       print("Please Enter An Integer")
       continue
    else:
        break

def fibIter(n):
  prePreFib = 1
  preFib = 1
  integer_list.append(prePreFib)
  integer_list.append(preFib)
  while len(integer_list) < n:
    nextFib = preFib + prePreFib
    integer_list.append(nextFib)
    prePreFib = preFib
    preFib = nextFib

fibIter(user_input)
print("Number ", user_input, " of the Fibonacci sequence is ", integer_list[-1])