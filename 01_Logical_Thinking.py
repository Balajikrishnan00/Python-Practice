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
'''
# 1.5p
c=5

a=22*c/7
b=22*(c/7)
print('a=%f\nb=%d\nc=%.2f'%(a,b,c))



