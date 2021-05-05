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

r=float(input('Enter  Radius of Cone:'))
h=float(input('Enter Height of Cone:'))
v= 1.0/3 * 22.0/7 * r * r * h
print('The Volume of Cone:%.2f'%v)
--------------------------------------------
# 3.2 p
The lowest temperature ever recorded in Antarctic is -126.9 Fahrenheit. Write a Program to convert this Temperature in
degrees Centigrade and print the result with appropriate captions. the formula is:
c= 5/9(F-32)


Location=input('Enter Location Name :')
F=float(input('Fahrenheit Temperature:'))
C= 5/9*(F-32.0)
print('The %s of degrees Centigrade     :%.2f C'%(Location,C))
-------------------------------------------------
# 3.3 p
write a program to compute and print the length of the hypotenuse of a right triangle,given its two legs
A and B. print the results with appropriate captions

import math
a=float(input('Enter A value:'))
b=float(input('Enter B value:'))
c=math.sqrt((a*a)+(b*b))
print('length of the hypotenuse:',c)
-------------------------------------
# 3.4p
write a program to approximate the Julian Date(introduced by julius Caesar in 46 B.C)
Equivalent to the calender date given in the form month,day.The Julian date 23 is the
day of year. January 1 has Julian date 1, February 2 has Julian Date 33,
December 31 has Julian Date 365, etc A formula to Approximate the
Julian date is (month -1) * 30+day determine the julian date for the given Month and Day.

day=int(input('Enter a Date:'))
month=int(input('Enter a Month:'))

julian=(month-1)*30+day
print(julian)
-----------------------------------------
#3.5p


strB=
BBBBBB
BBB  B
BBBBBB
BBBBBB


-----------------------------------------
# 3.5
Mr.x is a bricklayer. last year his gross pay was XGrossPay.after deducting 6.85% for social security and 23.5%
for federal income tax from his gross pay was his net income grater than Mrs y's net income?

Mrs. Y is a teacher who grossed YGrossPay but had $850.45 deducted for her income retirement plan and
16.3% of her gross income deducted for income tax purposes.print the salaries of mr.x and y
(test the program with XGrossPay as $23,564.99 and YGrossPay as $19,874
'''
XGrossPay=23564.99
XSocial=XGrossPay*6.85/100
XTax=XGrossPay*23.5/100
Xnet=XGrossPay-XSocial-XTax
print('Xnet:%.2f'%Xnet)

YGrossPay=19874
YDetection=850.45
Ytax=YGrossPay*16.3/100
Ynet=YGrossPay-YDetection-Ytax
print(Ynet)
