# https://www.practicepython.org/exercise/2022/03/06/38-f-strings.html

name = input("Hi, what is your name? ")
age = int(input(f"How old are you {name}? "))

current_year = 2026
age_difference = 100 - age 

final_age = current_year + age_difference

print(f"{name} will be 100 years old in the year {final_age}")