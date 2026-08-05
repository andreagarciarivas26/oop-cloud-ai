def greet():
    name = input("What is your name? ")
    print("Hello,", name)

greet()

import math

def suma(c1,c2):    
    real = c1[0] + c2[1]
    imaginaria = c1[0] + c2[1]

    return (real, imaginaria)

print("La suma de los vectores complejos es", suma((-2,0),(5,-9)))



def resta(num1, num2):
   
    a1, b1 = num1
    a2, b2 = num2

    return (a1 - a2, b1 - b2)

print("La resta de los vectores complejos es:", resta((-2,0),(5,-9)))