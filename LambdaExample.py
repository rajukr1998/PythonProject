"""
A lambda function is a small anonymous function
================
lambda function Syntax:
lambda arguments: expression
"""
manohar = lambda x: x*2
mysum = lambda a, b: a+b

def ankit(n):
    return lambda a: n*a
mydoubler = ankit(2)
mytripler = ankit(3)
# mytripler = lambda a: 3*a

print(manohar(4))
print(mydoubler(5))
print(mysum(32,78))
print(mytripler(12))
