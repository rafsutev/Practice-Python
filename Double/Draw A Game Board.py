# https://www.practicepython.org/exercise/2014/12/27/24-draw-a-game-board.html

x = " ---"
y = "|   "

def create_board(n):

    for i in range(n):
        print(x*n)
        print(y*(n+1))
    
    print(x*n)

create_board(int(input("What board size would you like? ")))