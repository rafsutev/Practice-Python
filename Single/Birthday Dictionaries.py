# https://www.practicepython.org/exercise/2017/01/24/33-birthday-dictionaries.html

birthdays = {
    "benjamin franklin": "01/17/1706",
    "albert einstein": "03/14/1879",
    "mark zuckerberg": "05/14/1984",
    "sofia bazdaric": "03/23/2001"
}

print("Welcome to the birthday dictonary here is who we have on record:")
for key in birthdays.keys():
    print(key.upper())
    
user_choice = input("Please enter a name: ").lower()

if user_choice in birthdays:
    print(f"Here is the birthday for your selection: {birthdays[user_choice]}")
else:
    print("Invalid option.") 



