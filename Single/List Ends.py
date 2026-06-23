# https://www.practicepython.org/exercise/2014/04/25/12-list-ends.html

a = [2, 5, 10, 15, 20, 25, 70, 99, 200, 109238]

new_list = []

def create_list():
    new_list.append(a[0])
    new_list.append(a[len(a)-1])
    print(new_list)

create_list()
