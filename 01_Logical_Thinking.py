"""
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
# 4.1P
Mr.x is a bricklayer. last year his gross pay was XGrossPay.after deducting 6.85% for social security and 23.5%
for federal income tax from his gross pay was his net income grater than Mrs y's net income?

Mrs. Y is a teacher who grossed YGrossPay but had $850.45 deducted for her income retirement plan and
16.3% of her gross income deducted for income tax purposes.print the salaries of mr.x and y
(test the program with XGrossPay as $23,564.99 and YGrossPay as $19,874

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
--------------------------------------
# 4.2p
The truth in lending law requires that money-lending institutions disclose the annual interest rate charged on
loans the approximate rate is given by the formula
R=(2+N)*F/P(n+1)
where N is the number of payments per year,
F=the finance charge in dollars,
P is the principle and
n=the number of scheduled installments payments, Write a program to determine the annual percentage rate for a loan
(Test values:P=$50000,36 Months repayments period, n=$162.50 per month, Finance charge=36*162.5-5000=$850)

P=float(input('Enter Principle amount:'))

N=int(input('No of Payment per Year:'))

n=float(input('No of Scheduled Payments:'))

mp=float(input('Payments / Installment:'))

tCollection=n*mp

F=tCollection-P

r= (2 + N) *F / (P*(1+n)) * 100

print('Rate of Interest:%.2f'%r)
-------------------------------------------------
#  4.3p
Miss T.drove X miles in Y hours and Spent Z for gas. Her car averages 14.5 miles per gallon write a program
to compute her average speed number of gallon used and the average cost per gallon the output should be as follows
(Test values:
X =1050 miles,
Y =17 1/2 hours,
Z =$86.75)


xmiles=1050

yhours=17.5

zcost=86.75

aSpeed=(xmiles / yhours)

nGallon=int(xmiles/14.5)

Gallon=zcost/nGallon



#print('Miles =          XXXX')
print('Miles =\t\t\t%5.0f km'%xmiles)


#print('Hours Driven =     YY.YY')
print('Hours Driven =\t%5.0f Hours'%yhours)

#print('Gas Cost =        ZZZ.ZZ')
print('Gas Cost =\t\t%8.2f'%zcost)

#print('Average Speed =   ---.--')
print('Average Speed =\t%5.0f kmph'%aSpeed)

#print('No. Gallons =     ---.--')
print('No. Gallons =\t%5.0f'%nGallon)

#print('Cost/Gallon =     ---.--')

print('Cost/Gallon =\t%8.2f'%Gallon)
-------------------------------------------------
# 4.4 p
write a program to produce exactly the following report on the cost c of operating technical
devices
        Cost Analysis

Watts   Hours       Cost/KW     Cost
65        6           .087      ---
100       6           .087      ---

The formula is
                C=Wtk/1000
                (where W=number of watts,T=time in hours,k=cost in cents per kilowatt hours)


W1=65
W2=100
t=6
rate=87
c1=W1*t*rate/1000
c2=W2*t*rate/1000
#print(c1)
#print(c2)
print('\t\t   COST ANALYSIS')
print('watts\tHours\t\tHours\\KW\tCost')
print(' 65\t\t  6\t\t\t .087\t\t%.2f'%c1)
print(' 65\t\t  6\t\t\t .087\t\t%.2f'%c2)
-----------------------------------------
# 4.5p
the date for any Easter Sunday can be computed as follows.Let N be the year for which Easter Sunday is to
be computed.
Let NA be the remainder of the division of N by 19.
Let NB be the remainder of the division of N by 4.
Let NC be the remainder of the division of N by 7.
Let ND be the remainder of the division of(19.NA.+24)by 30.
Let NE be the remainder of the division of(2.NB+4.NC+6ND+5)by 7.

the date for Easter Sunday is then March(22.ND+NE).Note that this can give a date in April

Write a program to read a year N and compute the date for Easter Sunday for that year using
    the formula 22+ND+NE.The resulting day can be in either March or April


N=int(input('Enter a Year:'))

NA= N % 19

NB= N % 4

NC= N % 7

ND= (19 * NA + 24) % 30

NE=(2 * NB + 4 * NC + 6 * ND + 5) % 7

eSunday=22 + ND + NE


if eSunday<=31:
    print('Easter Sunday of %d is March %d'%(N,eSunday))
else:
    print('Easter Sunday of %d is April %d'%(N,eSunday-31))
--------------------------------------------------------
# 5.1p
T seconds after dropping a stone into a well the stone hits the surface of the water Determine the height of the well
given the formula d=1/2 gT**2 where d is the distance,g is the force of gravity(9.81 meter/s),and
T is the time in seconds.(Use 15 seconds for testing your program)


t=int(input('Enter the number seconds to reach the water surface:'))


d=1/2*9.81*t*t
print(d)
-----------------------------
# 5.2p
for four resisters R1,R2,R3 and R4 in parallel the overall resistance R is given by:

1/R= 1/R1 + 1/R2 + 1/R3 + 1/R4

write a program to computeR and print the result as follows:(Use 1.5,3,4.5 6 ohms for R1,R2,R3,and R4 respectively
for testing your program)

R1=xx.x         R2=xx.x         R3=xx.x         R4=xx.x
the overall resistance R=xx.x

r1=1.5
r2=3
r3=4.5
r4=6
r=1/r1 + 1/r2 + 1/r3 + 1/r4
#print(1/r)
print('R1=%5.2f\t\tR2=%5.2f\t\tR3=%5.2f\t\tR4=%5.2f'%(r1,r2,r3,r4))
print('the overall resistance %.4f'%(1/r))
--------------------------------------------
"""

