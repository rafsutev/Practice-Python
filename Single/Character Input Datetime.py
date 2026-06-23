# https://www.practicepython.org/exercise/2022/03/20/39-character-input-datetime.html

from datetime import datetime

name = input("Hi, what is your name? ")
age = int(input(f"How old are you {name}? "))

current_year = datetime.now().year
age_difference = 100 - age 

final_age = current_year + age_difference

print(f"{name} will be 100 years old in the year {final_age}")