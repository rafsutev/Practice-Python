# https://www.practicepython.org/exercise/2014/02/15/03-list-less-than-ten.html

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
new_list = []

# Check every element in the list "a" and check if they're less than 5 then add it to the empty list "new_list"
for letter in a:
    if letter <= 5:
        new_list.append(letter)

print(f"Here is the new list of numbers less than five: {new_list}")

# Checks for any elements less than the number specified  
def user_choice(selection):
    user_list = []
    for letter in a:
        if letter <= selection:
            user_list.append(letter)
        
    print(f"Here are the numbers less than {selection}: {user_list}")

user_num = int(input("Please select a number: "))
user_choice(user_num)