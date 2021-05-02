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

# 1.3p
c=1.5
a=c
b=a*5
c=a+b
print('{}:{}:{}'.format(int(a),int(b),c))

# 1.4p
c=5
a=(22/7)*c
b=(22.0/7)*c

print('a:%.2f'%a)
print('b:%i'%b)
print('c:%.2f'%c)

# 1.5p
c=5

a=22*c/7
b=22*(c/7)
print('a=%f\nb=%d\nc=%.2f'%(a,b,c))

# 1.6p
r=3.75
a=22/7.0*r*r
c=2*3.17*r
print('Circle Calculator')
print('Given Radius of Circle   :%.4f'%r)
print('Area of Given Circle     :%.4f'%a)
print('Circumference            :%.4f'%c)

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

# 2.2p
write a program to read add the value of p,r,t,Calculate and display the simple interst using the
formula i=prt. write the output with approprite headings.
'''
p=50000
r=9.5/100
t=5

si=p*r*t
print('Principle amount is:',si)

