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
-------------------"""
