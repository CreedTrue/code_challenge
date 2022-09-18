# This program will take 3 integers as imput and then display the largest of the 3.

#starting variable/lists
int_list = []

#function to get input of only integers from user
def get_input():
    while True:
        try:
            user_input = int(input("What integer would you like to find the factorial of? "))
            int_list.append(user_input)
        except ValueError:
            print("Please Enter An Integer")
            continue
        else:
            break

#gets the 3 inputs of integers from the user
for x in range(3):
    get_input()

#sorts list so that the largest Integer will be at the last position
int_list.sort()

#prints largest Integer
print("The Largest Integer is: ", int_list[-1])
