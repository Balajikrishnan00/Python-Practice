""""-----------------------------------
# capital
name='balajikrishnan'

def Capital(name):
    return name[0].upper() + name[1:]

print(Capital(name))
_______________________________________
name='Python Is Very Easy'
print(name.casefold())
______________________________________
name='python'
#name='Python Is Very Easy'
#print(name.center(1,''))
prefunction=dir(str)
No_of_Function=0
for function in prefunction:
    if not function.startswith('__'):
        No_of_Function+=1
        print(function)
print('Total Predefined Functions is ',No_of_Function)
-------------------------------------"""
