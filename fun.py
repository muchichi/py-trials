from turtle import *

def main():
    #turtleI()
    star()

def turtleI():
    color('blue','blue')
    begin_fill()
    while True:
        forward(150)
        left(123)
        if abs(pos()) < 2:
            break
        end_fill()
    done()
    
def star():
    color('red','white')
    #st = turtle.Turtle()
    for i in range(5):
        forward(200)
        right(130)
        
    done()
    
    
if __name__ == '__main__': main()