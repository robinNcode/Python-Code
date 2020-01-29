t=int(input())

for i in range(1,t+1,1):
	n=int(input())
	
	if n>0 and n<32:
		a=pow(2,n)
		print(a-1)
		