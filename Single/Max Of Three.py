# https://www.practicepython.org/exercise/2016/03/27/28-max-of-three.html

def max_num(one,two,three):
    nums = [one, two, three]
    max = 0

    for i in nums:
        if i > max:
            max = i

    print(f"The largest of the three is {max}.")

max_num(10000,999,30)
    
 

    
    


        
