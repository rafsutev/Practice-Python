# https://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html

user_num = int(input("Please enter a number: "))

if user_num % 2 == 0:
    print("Your number is even.")

else:
    print("Your number is odd.")

if user_num % 14 ==0:
    print("Your number is also divisble by 4.")