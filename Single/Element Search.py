# https://www.practicepython.org/exercise/2014/11/11/20-element-search.html

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

user_num = int(input("Please select a number: "))

def number_match(num):
    if num in list:
        print(True)
        print("Your chosen number is on the list.")
    else:
        print(False)
        print("Your chosen number is not on the list.")

number_match(user_num)