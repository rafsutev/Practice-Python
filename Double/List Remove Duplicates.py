# https://www.practicepython.org/exercise/2014/05/15/14-list-remove-duplicates.html

a = [1,1,2,2,3,3,4,5,6]

def remove_dupes(set):
    new_list = []
    for element in set:
            if element not in new_list:
                  new_list.append(element)
    print(new_list)

remove_dupes(a)


