
a=int(input())
b=int(input())

if a<b:
	i=a
	while i<=b:
		j=1
		sum=0
		while j<=i:
			if i%j==0:
				sum=sum+j
			j+=1
		if sum==1:
			print(i,"is a Prime Number!!")
			sum=0
		
		elif sum==i+1:
			print(i,"is a Prime Number!!")
			
		
		else:
			print(i,"is not a Prime Number..")
			
		i+=1
else:
	i=b
	while i<=a:
		j=1
		sum=0
		while j<=i:
			if i%j==0:
				sum=sum+j
			j+=1
		if sum==1:
			print(i,"is a Prime Number!!")
			sum=0
		
		elif sum==i+1:
			print(i,"is a Prime Number!!")
			
		
		else:
			print(i,"is not a Prime Number..")
			
		i+=1			