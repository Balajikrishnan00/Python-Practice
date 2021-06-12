"""
prefunction=dir(str)

#print(prefunction)
for x in prefunction:
    if not x.startswith('__'):
        print(x)
______________________"""
name='krishnan'
#print(name.capitalize())
# user Make it
# string is immutable How we can make user method
class StringMethod:
    def __init__(self,name):
        self.name=name
    def Capital(self):
        return self.name[0].upper()+self.name[1:]

n1=StringMethod(name)
print(n1.Capital())
