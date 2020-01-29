#Square series..
#1*1+2*2+3*3+.......+n*n

n=int(input("Enter the last number :"))

for x in range(1,n+1,1):
	print(x)
	
print()

for x in range(1,n+1,1):
	x=x*x
	print(x)