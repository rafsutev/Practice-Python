# https://www.practicepython.org/exercise/2014/03/12/06-string-lists.html

user_string = input("Please enter a word: ").lower()

def check_palindrome(string):
    reversed = string[::-1]
    
    if reversed == string:
        print("This is a palindrome")
    else:
        print("This is not a palindrome")

check_palindrome(user_string)