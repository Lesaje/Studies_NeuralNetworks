import random
import numpy as np

def horner_func(x, coef):
    p = 0
    degree = len(coef)
    for i in range(degree):
        p = p*x + coef[i]
    return p

print ("Please, insert coefficients of P(x). If P(x) has the form x^2 + 2, take the coefficients equal 1 0 2")
coefficents = list(map(float, input().split()))
DEG = len(coefficents) - 1                                           #max degree of polinom
derivativecoef = []
degTEMP = DEG
for i in range(DEG):
    derivativecoef.append(coefficents[i]*degTEMP)           
    degTEMP -= 1
A = abs(max(derivativecoef, key=abs))
FIRST_Element = derivativecoef[0]
UPBorder = round(1 + A/(abs(FIRST_Element))+0.5)                    #calculate the boundaries of the roots of the derivative.
LOWBorder = round(-(1 + A/(abs(FIRST_Element)))-0.5)         #rounding to bigger/smaller number
BETA = UPBorder + abs(LOWBorder)
STEP_SIZE = BETA/10000                                   #Just nice to me step size. Can be changed if works slowly to 1000
minimums = []
EPS = 1
for previous_x in range (LOWBorder, UPBorder):
    while (EPS>10**(-10)):                                                      #can be changed if works slowly to -5 without huge loss of precision
        current_x = previous_x - STEP_SIZE * horner_func(previous_x, derivativecoef)
        EPS = abs(previous_x - current_x)
        previous_x = current_x
    minimums.append(current_x)
values = []
for i in range (len(minimums)):
    values.append(horner_func(minimums[i], coefficents))
print ("Minima of this polynomial: ", min(values))

