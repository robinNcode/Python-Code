
while 1:
	
	n=int(input("Enter a number:"))
	sum=0
	i=1
	while i<=n:
		
		if n%i==0:
			sum=sum+i
		i+=1
			
	if sum==1:
		print(n,"is a Prime Number!!")
		
	elif sum==n+1:
		print(n,"is a Prime Number!!")
		
	else:
		print(n,"is not a Prime Number.")
		
