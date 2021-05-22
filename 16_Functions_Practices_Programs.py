"""
# 1 maximun of two  numbers

def maxofTwoNumbers(a,b):
    if a>b:
        return a
    else:
        return b
n1=int(input('Enter A Number:'))
n2=int(input('Enter B Number:'))
result=maxofTwoNumbers(n1,n2)
print(result)
-------------------
# 2  Factorial

def Factorial(n):
    return n if (n==0 or n==1) else n* Factorial(n-1)

num=int(input('Enter a num:'))
result=Factorial(num)
print(result)
-------------------
# 3 simple interest
#   A = P(1 + R/100) ** t
#   Compound Interest = A – P
import math
def CompountInterest(P,R,T):
    A=P*(pow(1+(R/100),T))
    CI=round(A-P)
    print('INR %.2f'%CI)
P=10000
R=10.25
T=5
CompountInterest(P,R,T)

#print(math.pow(4,2))
___________________________________"""
# Find the length of the list and simply swap the first element with (n-1)th element.
l=[12,32,45,61,77]

def swap(uploadeList):
    length=len(l)
    uploadeList[0],uploadeList[length-1]=uploadeList[length-1],uploadeList[0]
    return uploadeList
print(swap(l))
