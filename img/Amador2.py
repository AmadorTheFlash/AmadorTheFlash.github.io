print("enter  a nmuber and i will double it")
x=int(input())

if x%2==0:
    print("this number is even")
else:
    print(" this number is odd")

def double(x):
    y= 2 * x
    return y
print(" twice your number is " + str(double(x)))



print("let us draw a square. How big shall we draw a square?")

x=int(input())
import turtle
perty=turtle.Turtle()

for i in range(4):
    perty.forward(x)
    perty.right(90)
    
