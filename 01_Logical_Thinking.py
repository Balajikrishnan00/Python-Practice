'''
# 1.1p
a=10
b=20
a=a+b
print('a:',id(a))
b=a-b
print('b:',id(b))
a=a-b
print('a:',id(a))
print(a)
print('a:',id(a))
print(b)
print('b:',id(b))
------------------------------------------------------
# 1.2p
a=5
b=10
a=a+a
#print(f'%i+%i={a+b}'%(a,b))
#print('{}+{}={}'.format(a,b,a+b))
b=b+b
#print('{}+{}={}'.format(a,b,a+b))

a=a*b
#print('a=%i'%a)
b=a-b
#print('b=%i'%b)
print('a=%i b=%i'%(a,b))
----------------------------------------------
# 1.3p
c=1.5
a=c
b=a*5
c=a+b
print('{}:{}:{}'.format(int(a),int(b),c))
--------------------------------------------------
# 1.4p
c=5
a=(22/7)*c
b=(22.0/7)*c

print('a:%.2f'%a)
print('b:%i'%b)
print('c:%.2f'%c)
-------------------------------------------------
# 1.5p
c=5

a=22*c/7
b=22*(c/7)
print('a=%f\nb=%d\nc=%.2f'%(a,b,c))
-----------------------------------------------
# 1.6p
r=3.75
a=22/7.0*r*r
c=2*3.17*r
print('Circle Calculator')
print('Given Radius of Circle   :%.4f'%r)
print('Area of Given Circle     :%.4f'%a)
print('Circumference            :%.4f'%c)
----------------------------------------------------
# 2.1p
write a program to read integers A and B produce the remainder (expressed as an integer) of
A/B for example the remainder of 13/2 is 1. while the remainder of 29/6 is 5.
(note: Don't use the % opetator)

a=int(input('Enter A vaule:')
b=int(input('Enter B value:')
c=a//b #6

d=c*b
e=a-d
print('%i/%i=%i'%(a,b,e))
-----------------------------------------------------
# 2.2p
write a program to read add the value of p,r,t,Calculate and display the simple interst using the
formula i=prt. write the output with approprite headings.

p=int(input('Enter Principle Amount     :'))
r=float(input('Enter rate of Interest   :'))

t=int(input('Enter no of Years'))

si=p*r/100*t
print('Principle amount is:',si)
----------------------------------------------------------
# 2.3p
with an interest rate I and a Principal P deposited for N Year period in a savings account write
a program to compute a total principal T,given the formula:T=P(1+I)pow N

# I=rate of interest , P=depositer amount , N= no of Years
P=50000
I=9.5
N=5
T=P*(1+I/100)**N
print('Total value:%.2f'%T)
Ins=P-T
print('rate of interest:%.2f'%Ins)
----------------------------------------------------------
# 2.4p
Suppose the interest of 2.3 is compounded daily.write a program to compute:
the total principle given by the formula

T=P(1+I/J)**J-N

where J is the number of times the interest is compounded per year compute and print
the difference between total amounts when the principle ia compounded once and 365 times a year,
also print the corresponding interests.


P=50000
R=9.5
N=5
J=365
T1=P*(1+(R/100)/365)**(N*J)
print(' Daily Total value:%.2f'%T1)
J=1
T2=P*(1+(R/100)/365)**(N*J)
print('Yearly total value:%.2f'%T2)
-------------------------------------------
# 2.5
A wholesaler accepts an amount P as promissory note at 7% in lieu of cash payment for delivered goods.
write a program to compute the maturity value of the note for a 30,60 and 90 90-day short-term loan.The formula
to compute the maturity value S is:
S=P(1+I*N)
where P is the principle l is the interest rate and N is the number of years
(expressed N as number of days divide by 360)

N1=30/360
N2=60/360
N3=90/360
P=int(input('Enter Principle Amount:'))

I=7/100
S_30=P*(1+I*N1)
S_60=P*(1+I*N2)
S_90=P*(1+I*N3)
print('The Amount of 30 Days:%.2f'%S_30)
print('The Amount of 60 Days:%.2f'%S_60)
print('The Amount of 90 Days:%.2f'%S_90)
---------------------------------------------------
# 3.1p
write a program to find the volume of a cone using the formula:
v=1/3 * pi * r * r * h
'''
r=float(input('Enter  Radius of Cone:'))
h=float(input('Enter Height of Cone:'))
v= 1.0/3 * 22.0/7 * r * r * h
print('The Volume of Cone:%.2f'%v)


