# https://www.practicepython.org/exercise/2014/04/30/13-fibonacci.html

def fibonacci(n):
    previous = 0
    current = 1

    for i in range(n):
    
        new_num = current + previous
        print(new_num)
    
        current = previous
        previous = new_num

fibonacci(int(input("How many Fibonacci numbers would you like? ")))