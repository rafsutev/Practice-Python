# https://www.practicepython.org/exercise/2014/02/26/04-divisors.html

user_num = int(input("Please enter a number: "))
x = range(1, user_num+1)
list = []

for num in x:
    if user_num % num == 0:
        list.append(num)
    
print(list)
