# https://www.practicepython.org/exercise/2014/01/29/01-character-input.html

name = input("Hi, what is your name? ")
age = int(input("How old are you " + name + "? "))

current_year = 2026
age_difference = 100 - age 

final_age = str(current_year + age_difference)

print(name + " will be 100 years old in the year " + final_age)
