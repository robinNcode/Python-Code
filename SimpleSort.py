'''MsM Robin
   Sonargaon University
   Date:8/14/19
'''
from math import *

a=int(input())

b=int(input())

c=int(input())

y=max(a,b)
y=max(y,c)

x=min(a,b)
x=min(x,c)


if a==x and b==y or b==x and a==y:
	print(x)
	print(c)
	print(y)


elif b==x and c==y or c==x and b==y:
	print(x)
	print(a)
	print(y)

elif a==x and c==y or c==x and a==y:
	print(x)
	print(b)
	print(y)

print()
print(a)
print(b)
print(c)